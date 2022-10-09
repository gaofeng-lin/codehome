package lrufunc

import (
	"io"
)
// 参考：https://sourcegraph.com/github.com/google/leveldb/-/blob/include/leveldb/cache.h
type Cache interface{
// 在multiple clients下共享相同的cache来划分key空间
// 当启动是会被分配一个新id 
NewId()  uint64 

// 插入: 从 key-value到cache的映射
// 当insert的entry不在需要时对应的key-value传给deleter处理
Insert(key string, value interface{}, size int, deleter func(key string, value interface{})) (handle io.Closer)

// 查找: 不存在时返回 nil，nil， false
Lookup(key string) (value interface{}, handle io.Closer, ok bool)

// 删除: 注意必须所有关联的handle释放才能erase key
Erase(key string)

// 关闭: 所有的handle必须release 才能destroy所有存在的entries
Close()  error
}