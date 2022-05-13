package Test;

class Solution {
    public Node getKthFromEnd(Node head, int k) {
        Node tmp=head;
        int count=0;

        while(tmp!=null){
            count++;
            tmp=tmp.next;
        }

        if(k>count){
            return null;
        }

        int num_delete=count-k;

        Node form=head;
        while(num_delete!=0){

            form=form.next;
            num_delete=num_delete-1;
        }
        return form;
    }
}


public class Test {

        public static void main(String[] args) {
            MyLinkedList myLinkedList = new MyLinkedList();
            myLinkedList.addNode(9);
            myLinkedList.addNode(8);
            myLinkedList.addNode(6);
            myLinkedList.addNode(3);
            myLinkedList.addNode(5);

            //打印链表
            myLinkedList.printLink();

            Node head = myLinkedList.getHeadNode();
//            System.out.print(head);
            Solution s = new Solution();

            Node s1 = s.getKthFromEnd(head,2);

            System.out.print(s1);
        }

}