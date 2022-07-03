package Tree;

class Node{
    int val;
    Node left;
    Node right;
    Node(int v){
        this.val = v;
    }
}

class Tree{
    Node root;
    int size = 0;
    Node find_node;
    Tree(int val){
        root = new Node(val);
        root.left = null;
        root.right = null;
        size++;
    }

    void findInsertLocation(Node tmp){
        if(tmp.left==null||tmp.right==null){
            find_node = tmp;
            return ;
        }
        findInsertLocation(tmp.left);
        findInsertLocation(tmp.right);
//        return tmp;
    }

    //插入函数按照完全二叉树来
//    要调用一个遍历函数
    void insert(int val){
        Node tmp = root;
        findInsertLocation(tmp);
        if(find_node.left==null){
            Node newOne  = new Node(val);
            find_node.left = newOne;
            newOne.left = null;
            newOne.right = null;
        }else{
            Node newOne  = new Node(val);
            find_node.right = newOne;
            newOne.left = null;
            newOne.right = null;

        }
    }

    Node getRoot(){
        return root;
    }

    void print(Node tmp){
        if(tmp==null){
            return ;
        }
        System.out.println(tmp.val);
        print(tmp.left);
        print(tmp.right);
    }

}

public class Main {
    public static void main(String[] args) {
        Tree tree = new Tree(1);
//        Node root =
//        Node tmp = root;
        tree.insert(5);
        tree.insert(4);
        tree.insert(20);
        tree.print(tree.getRoot());
    }
}