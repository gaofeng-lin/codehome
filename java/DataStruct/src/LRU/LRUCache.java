package LRU;

import java.util.HashMap;
import java.util.HashSet;

class Node{
    public int key, val;
    public Node next, pre;
    public Node(int k, int v) {
        this.key = k;
        this.val = v;
    }
}

class DoubleList{
    public Node head, tail;
    public int len;

    public DoubleList() {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.pre = head;
        this.len = 0;
    }
    //    在链表头部插入节点
    public void addFirst(Node x) {
        x.next = head.next;
        head.next.pre = x;
        head.next = x;
        x.pre = head;
        len++;
    }
    //    删除链表任意一个节点。如果get到了一个已经存在的，要把它提出来，添加到头部。首先需要删除
    public void remove(Node x) {
        x.pre.next = x.next;
        x.next.pre = x.pre;
        len--;
    }
    //    尾节点删除，表示过期
    public Node removeLast() {
        if(head.next == tail){
            return null;
        }
        Node del = tail.pre;
        remove(del);
        return del;
    }
    //    返回当前长度
    public int size() {
        return len;
    }
}


public class LRUCache {

    private HashMap<Integer, Node> map;
    private DoubleList cache;
    public int cap;

    public LRUCache(int capacity) {
        this.cap = capacity;
        map = new HashMap<>();
        cache = new DoubleList();
    }
    //    将某个节点提升到头部
    public void makeRencently(int key) {
        Node x = map.get(key);
        cache.remove(x);
        cache.addFirst(x);
    }

    public int get(int key) {
        if(!map.containsKey(key)) {
            return -1;
        }
        makeRencently(key);
        return map.get(key).val;
    }

    public void deleteKey(int key) {
        Node x = map.get(key);
        cache.remove(x);
        map.remove(key);
    }

    public void addRencently(int key, int val) {
        Node x = new Node(key, val);
        cache.addFirst(x);
        map.put(key, x);
    }

    public void removeLeastRecently() {
        Node x = cache.removeLast();
        int k = x.key;
        map.remove(k);
    }

    public void put(int key, int value) {
//        赋予新的值，提升到头部
        if(map.containsKey(key)) {
//            修改值
            deleteKey(key);
            addRencently(key, value);
            return ;
        }

        if(cap == cache.size()){
//            删除最久没使用的
            removeLeastRecently();
        }

        addRencently(key,value);
    }

    public static void main(String[] args) {
        LRUCache lru = new LRUCache(2);
        lru.put(1, 12);
        lru.put(2, 2);
        System.out.println(lru.get(1));
    }

}

