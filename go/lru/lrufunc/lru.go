package lrufunc
import (
	"container/list"
	"fmt"
	"io"
	"runtime"
	"sync"
	"sync/atomic"
	"time"
	"github.com/hedzr/assert"
  )
  
  var _Cache = (*LRUCache)(nil)
  
  // LRU cache实现
  type   LRUCache struct{
	  * _LRUCache
  }
  
  type _LRUCache struct{
	 mu  sync.Mutex
	 //  采用双向链表  和 HashTable
	 //  双向循环链表，有大小限制，保证数据的新旧，当缓存不够时，保证先清除旧的数据
	 list     *list.List
  
	 // 二级指针数组，链表没有大小限制，动态扩展大小，保证数据快速查找，hash定位一级指针，得到存放在一级指针上的二级指针链表，遍历查找数据
	 table  map[string]*list.Element
  
	 // 当前size
	 // cache容量
	 size         int64
	 capacity  int64
	 last_id     uint64
  }
  
  // handle to an entry： 
  // 哈希表中的元素
  type LRUHandle struct{
	  c                      *LRUCache
	  key                   string
	  value                interface{}
	  size                   int64
	  deleter              func(key string, vlaue interface{})
	  time_created    time.Time
	  time_accessed atomic.Value
	  refs                    uint32
  }
  //  获取key
  func   (h *LRUHandle)  Key()  string{
	return h.key
  }
  
  // 获取value
  func (h *LRUHandle) Value() interface{} {
	  return h.value
  }
  // 获取size
  func (h *LRUHandle) Size() int {
	  return int(h.size)
  }
  
  // 获取entry创建时间
  func (h *LRUHandle) TimeCreated() time.Time {
	  return h.time_created
  }
  
  // 获取entry访问时间
  func (h *LRUHandle) TimeAccessed() time.Time {
	  return h.time_accessed.Load().(time.Time)
  }
  
  // 
  func (h *LRUHandle) Retain() (handle *LRUHandle) {
	  h.c.mu.Lock()
	  defer h.c.mu.Unlock()
	  h.c.addref(h)
	  return h
  }
  
  func (h *LRUHandle) Close() error {
	  h.c.mu.Lock()
	  defer h.c.mu.Unlock()
	  h.c.unref(h)
	  return nil
  }
  
  //=================华丽分割线=================
  // 根据指定capacity新建一个cache
  func NewLRUCache(capacity int64) *LRUCache {
	//   assert(capacity > 0)
	  p := &_LRUCache{
		  list:     list.New(),
		  table:    make(map[string]*list.Element),
		  capacity: capacity,
	  }
	  runtime.SetFinalizer(p, (*_LRUCache).Close)
	  return &LRUCache{p}
  }
  
  // 清除所有已存在的entry通过deleter函数(用户自定义)
  // 前提：所有的handle必须release
  func (p *LRUCache) Close() error {
	  runtime.SetFinalizer(p._LRUCache, nil)
	  p._LRUCache.Close()
	  return nil
  }
  
  // 获取cache中key对应的内容 
  func (p *LRUCache) Get(key string) (value interface{}, ok bool) {
	  if v, h, ok := p.Lookup(key); ok {
		  h.Close()
		  return v, ok
	  }
	  return
  }
  
  // 类似get，差异在于cache中不存在时，可交由用户自行处理返回结果同时将返回的结果存放到cache中
  func (p *LRUCache) GetFrom(key string, getter func(key string) (v interface{}, size int, err error)) (value interface{}, err error) {
	  if v, h, ok := p.Lookup(key); ok {
		  h.Close()
		  return v, nil
	  }
	  if getter == nil {
		  return nil, fmt.Errorf("cache: %q not found!", key)
	  }
	  value, size, err := getter(key) // 由使用方自行处理 比如从其他存储介质获取
	  if err != nil {
		  return
	  }
	  assert(size > 0)
	  p.Set(key, value, size)   // 将内容添加到cache
	  return
  }
  
  // 获取value并指定默认值 当cache中不存在时返回第一个default值作为结果
  func (p *LRUCache) Value(key string, defaultValue ...interface{}) interface{} {
	  if v, h, ok := p.Lookup(key); ok {
		  h.Close()
		  return v
	  }
	  if len(defaultValue) > 0 {
		  return defaultValue[0]
	  } else {
		  return nil
	  }
  }
  
  // 添加key-value并指定size同时也设定deleter用于当key-value不用时执行delete
  func (p *LRUCache) Set(key string, value interface{}, size int, deleter ...func(key string, value interface{})) {
	  if len(deleter) > 0 {  // 给定deleter函数
		  h := p.Insert(key, value, size, deleter[0])
		  h.Close()
	  } else {
		  h := p.Insert(key, value, size, nil)
		  h.Close()
	  }
  }
  
  // 能够用于多clients共享相同的cache来分割key空间
  // 一般在启动时会分配一个新的id给client，可将id作为key的前缀
  func (p *LRUCache) NewId() uint64 {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  p.last_id++
	  return p.last_id
  }
  
  // 建立key-value到cache的映射并分配指定size
  //  返回操作该映射的handle 当映射不再被需要时handle.Close会被调用
  // 另外当insert的entry不再需要会触发deleter
  func (p *LRUCache) Insert(key string, value interface{}, size int, deleter func(key string, value interface{})) (handle io.Closer) {
	  handle = p.Insert_(key, value, size, deleter)
	  return
  }
  
  // 类似insert 不过返回值=LRUHandle
  func (p *LRUCache) Insert_(key string, value interface{}, size int, deleter func(key string, value interface{})) (handle *LRUHandle) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  assert(key != "" && size > 0)
		 // 当二级指针数组中已存在对应的key
		 // 需要先执行remove在table和list
		// 当缓存不够时  保证cache数据最新
	  if element := p.table[key]; element != nil {
		  p.list.Remove(element)  // 删除双向链表中element
		  delete(p.table, key) // 删除二级索引表
  
		  h := element.Value.(*LRUHandle) 
		  p.unref(h)                     // 解除引用
	  } 
		  
		  // 新建LRUHandle
	  h := &LRUHandle{
		  c:            p,
		  key:          key,
		  value:        value,
		  size:         int64(size),
		  deleter:      deleter,
		  time_created: time.Now(),
		  refs:         2, // One from LRUCache, one for the returned handle
	  }
	  h.time_accessed.Store(time.Now())
		  // 放置表头 最新的数据
	  element := p.list.PushFront(h)
	  p.table[key] = element
	  p.size += h.size
	  p.checkCapacity()  // 检查是否超过capacity
	  return h
  }
  
  // 查找
  // 若是cache中不存在对应key的内容返回nil，nil，false
  // 否则返回handle(key-value与cache的映射)
  // 当mapping不存需要时 需要调用handle.Close() 
  func (p *LRUCache) Lookup(key string) (value interface{}, handle io.Closer, ok bool) {
	  // warning: (*LRUHandle)(nil) != (io.Closer)(nil)
	  if v, h, ok := p.Lookup_(key); ok {
		  return v, h, ok
	  }
	  return
  }
  
  // 类似Lookup 但返回值 *LRUHandle.
  func (p *LRUCache) Lookup_(key string) (value interface{}, handle *LRUHandle, ok bool) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
		  // 通过二级索引数组 获取key的内容
	  element := p.table[key]
	  if element == nil {
		  return nil, nil, false
	  }
		  // 通过二级索引table查找到element 再将双向链表list中的element移到表头
	  p.list.MoveToFront(element)
		 // 获取到对应的元素
	  h := element.Value.(*LRUHandle)
	  h.time_accessed.Store(time.Now())
		 // 记录当前handle的引用数
	  p.addref(h)
	  return h.Value(), h, true
  }
  
  // 获取key对应的内容 并删除cache中双向链表和二级索引的内容
  func (p *LRUCache) Take(key string) (handle io.Closer, ok bool) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  element := p.table[key]
	  if element == nil {
		  return nil, false
	  }
		  // 删除双向链表对应的element
	  p.list.Remove(element)
		 // 删除二级索引中的记录
	  delete(p.table, key)
  
	  h := element.Value.(*LRUHandle)
	  return h, true
  }
  
  // 删除key ： 注意需要release所有关联的handle
  func (p *LRUCache) Erase(key string) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  element := p.table[key]
	  if element == nil {
		  return
	  }
		  // 删除list中的element和table中记录
	  p.list.Remove(element)
	  delete(p.table, key)
		 
	  h := element.Value.(*LRUHandle)
	  p.unref(h)       // 释放与handle的关联
	  return
  }
  
  // 设置cache的capacity
  // 当capacity过小且当前cache size远超过capacity时，cache将进行收缩
  func (p *LRUCache) SetCapacity(capacity int64) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  assert(capacity > 0)
	  p.capacity = capacity
	  p.checkCapacity()
  }
  
  // 返回cache的少量统计信息：
  // 当前entry的数量、cache size、cache capacity、最久访问entry的时间
  func (p *LRUCache) Stats() (length, size, capacity int64, oldest time.Time) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
	  if lastElem := p.list.Back(); lastElem != nil {
		  oldest = lastElem.Value.(*LRUHandle).time_accessed.Load().(time.Time)
	  }
	  return int64(p.list.Len()), p.size, p.capacity, oldest
  }
  
  // 统计信息以json串显示
  func (p *LRUCache) StatsJSON() string {
	  if p == nil {
		  return "{}"
	  }
	  l, s, c, o := p.Stats()
	  return fmt.Sprintf(`{
	  "Length": %v,
	  "Size": %v,
	  "Capacity": %v,
	  "OldestAccess": "%v"
  }`, l, s, c, o)
  }
  
  // cache中element的数量：
  func (p *LRUCache) Length() int64 {
	  p.mu.Lock()
	  defer p.mu.Unlock()
	  return int64(p.list.Len())
  }
  
  // 返回cache的size
  func (p *LRUCache) Size() int64 {
	  p.mu.Lock()
	  defer p.mu.Unlock()
	  return p.size
  }
  
  // 返回cache的capacity
  func (p *LRUCache) Capacity() int64 {
	  p.mu.Lock()
	  defer p.mu.Unlock()
	  return p.capacity
  }
  
  // 返回cache最新访问的element的time
  // 若是cache为空 则返回IsZero()的时间
  func (p *LRUCache) Newest() (newest time.Time) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
	  if frontElem := p.list.Front(); frontElem != nil {
		  newest = frontElem.Value.(*LRUHandle).time_accessed.Load().(time.Time)
	  }
	  return
  }
  
  // 返回cache最久访问的element的time
  // 若是cache为空 则返回IsZero()的时间
  func (p *LRUCache) Oldest() (oldest time.Time) {
	  p.mu.Lock()
	  defer p.mu.Unlock()
	  if lastElem := p.list.Back(); lastElem != nil {
		  oldest = lastElem.Value.(*LRUHandle).time_accessed.Load().(time.Time)
	  }
	  return
  }
  
  // 返回cache中最新使用key集合
  func (p *LRUCache) Keys() []string {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  keys := make([]string, 0, p.list.Len())
	  for e := p.list.Front(); e != nil; e = e.Next() {
		  keys = append(keys, e.Value.(*LRUHandle).key)
	  }
	  return keys
  }
  // LRUHandle引用计数（增加）
  func (p *_LRUCache) addref(h *LRUHandle) {
	  h.refs++
  }
  // LRUHandle引用计数（减少）
  func (p *_LRUCache) unref(h *LRUHandle) {
	  assert(h.refs > 0)
	  h.refs--
	  if h.refs <= 0 {
		  p.size -= h.size
		  if h.deleter != nil {
			  h.deleter(h.key, h.value)
		  }
	  }
  }
  
  // 检查capacity：压缩相对时间比较久的entry（剔除）
  func (p *LRUCache) checkCapacity() {
		  // 当cache的size大于capacity同时二级索引数组不止1个 进行shrank
		 // 从双向链表的尾部开始remove对应的element
		 // 同时二级索引数组对应的内容也需要delete 并减少对应的引用计数 
		// 直至size <= capacity 二级索引数组个数 = 1
	  for p.size > p.capacity && len(p.table) > 1 {
		  delElem := p.list.Back()
		  h := delElem.Value.(*LRUHandle)
		  p.list.Remove(delElem)
		  delete(p.table, h.key)
		  p.unref(h)
	  }
  }
  
  // 清空
  func (p *LRUCache) Clear() {
	  p.mu.Lock()
	  defer p.mu.Unlock()
		  // release 二级索引数组关联的handle
	  for _, element := range p.table {
		  h := element.Value.(*LRUHandle)
		  p.unref(h)
	  }
		  // cache的双向链表和二级索引数组置空
	  p.list = list.New()
	  p.table = make(map[string]*list.Element)
	  p.size = 0
	  return
  }
  
  //   cache的close
  func (p *_LRUCache) Close() {
	  p.mu.Lock()
	  defer p.mu.Unlock()
  
	  for _, element := range p.table {
		  h := element.Value.(*LRUHandle)
		  assert(h.refs == 1, "h.refs = ", h.refs)
		  p.unref(h)
	  }
  
	  p.list = nil
	  p.table = nil
	  p.size = 0
  }