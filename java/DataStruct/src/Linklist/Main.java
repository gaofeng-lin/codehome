package Linklist;

class Node{
    int val;
    Node next;
    Node(int v){
        this.val = v;
    }
}

class LinkList{
    Node head;
    int size;

    LinkList(){
        head =new Node(0);
        head.next = null;
        size = 0;
    }

    void addLast(int v){
        Node tmp_node = new Node(v);
        tmp_node.next = head.next;
        head.next=tmp_node;
        size++;
    }

//    是否包含某个元素
    boolean contains(int v){
        boolean flag = false;
        Node tmp = head.next;
        for(int i=0;i<size;i++){
//            System.out.println(tmp.val);
            if(tmp.val==v){
                flag = true;
                return flag;

            }
            tmp = tmp.next;
        }
        return flag;
    }

    String remove(int v){
        Node pre = head;
        Node cur = head.next;

        for(int i=0;i<size;i++){
            if (cur.val==v){
                pre.next = pre.next.next;
                cur.next = null;
                size--;
                return "元素"+v+"成功删除";

            }
            pre = pre.next;
            cur = cur.next;
        }


        return "该元素不存在";
    }


    void print(){
        Node tmp = head.next;
        for(int i=0;i<size;i++){
            System.out.println(tmp.val);
            tmp = tmp.next;
        }
    }

}

public class Main {
    public static void main(String[] args) {
        LinkList list = new LinkList();
        list.addLast(1);
        list.addLast(3);
        list.addLast(13);
        list.addLast(22);
        list.print();
//        System.out.println(list.contains(22));
        System.out.println(list.remove(13));
        list.print();
    }


}