package Test;

public class MyLinkedList {

    /**链表的头结点*/
    Node head = null;

    /**
     * 链表添加结点:
     * 找到链表的末尾结点，把新添加的数据作为末尾结点的后续结点
     * @param data
     */
    public void addNode(int data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;
        }
        Node temp = head;
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = newNode;
    }

    /**
     * 链表删除结点:
     * 把要删除结点的前结点指向要删除结点的后结点，即直接跳过待删除结点
     * @param index
     * @return
     */
    public boolean deleteNode(int index){
        if(index<1 || index>length()){//待删除结点不存在
            return false;
        }
        if(index == 1){//删除头结点
            head = head.next;
            return true;
        }
        Node preNode = head;
        Node curNode = preNode.next;
        int i = 1;
        while(curNode != null){
            if(i==index){//寻找到待删除结点
                preNode.next = curNode.next;//待删除结点的前结点指向待删除结点的后结点
                return true;
            }
            //当先结点和前结点同时向后移
            preNode = preNode.next;
            curNode = curNode.next;
            i++;
        }
        return true;
    }

    /**
     * 求链表的长度
     * @return
     */
    public int length(){
        int length = 0;
        Node curNode = head;
        while(curNode != null){
            length++;
            curNode = curNode.next;
        }
        return length;
    }

    /**
     * 链表结点排序,并返回排序后的头结点:
     * 选择排序算法,即每次都选出未排序结点中最小的结点，与第一个未排序结点交换
     * @return
     */
    public Node linkSort(){
        Node curNode = head;
        while(curNode != null){
            Node nextNode = curNode.next;
            while(nextNode != null){
                if(curNode.data > nextNode.data){
                    int temp = curNode.data;
                    curNode.data = nextNode.data;
                    nextNode.data = temp;
                }
                nextNode = nextNode.next;
            }
            curNode = curNode.next;
        }
        return head;
    }

    /**
     * 打印结点
     */
    public void printLink(){
        Node curNode = head;
        while(curNode !=null){
            System.out.print(curNode.data+" ");
            curNode = curNode.next;
        }
        System.out.println();
    }



    /**
     * 返回倒数第k个结点,
     * 两个指针，第一个指针向前移动k-1次，之后两个指针共同前进，
     * 当前面的指针到达末尾时，后面的指针所在的位置就是倒数第k个位置
     * @param k
     * @return
     */
    public Node findReverNode(int k){
        if(k<1 || k>length()){//第k个结点不存在
            return null;
        }
        Node first = head;
        Node second = head;
        for(int i=0; i<k-1; i++){//前移k-1步
            first = first.next;
        }
        while(first.next != null){
            first = first.next;
            second = second.next;
        }
        return second;
    }

    /**
     * 查找正数第k个元素
     */
    public Node findNode(int k){
        if(k<1 || k>length()){//不合法的k
            return null;
        }
        Node temp = head;
        for(int i = 0; i<k-1; i++){
            temp = temp.next;
        }
        return temp;
    }

    /**
     * 反转链表，在反转指针钱一定要保存下个结点的指针
     */
    public void reserveLink(){
        Node curNode = head;//头结点
        Node preNode = null;//前一个结点
        while(curNode != null){
            Node nextNode = curNode.next;//保留下一个结点
            curNode.next = preNode;//指针反转
            preNode = curNode;//前结点后移
            curNode = nextNode;//当前结点后移
        }
        head = preNode;
    }


    public Node getLastNode(){
        Node temp = head;
        while(temp.next != null){
            temp = temp.next;
        }
        return temp;
    }

    public Node getHeadNode(){
        return  head;
    }

}