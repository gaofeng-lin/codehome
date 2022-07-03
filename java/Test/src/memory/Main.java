package memory;

public class Main {

    public static void main(String[] args) {
        A a = new A(2,2);

        System.out.println("调用没有更改指向的方法前"+a);

        changeA1(a);

        System.out.println("调用没有更改指向的方法后"+a);

        System.out.println("调用更改指向的方法前"+a);

        changeA2(a);

        System.out.println("调用更改指向的方法后"+a);
    }

    public static void changeA1(A a){

    }
    public static void changeA2(A a){
        //刚传过来的a还是指向旧地址的a
        //但是方法内部在堆中创建了一个对象，并将a的指向指向新地址
        a = new A(20,20);

        System.out.println("更改指向后的新对象:"+a);
    }

}

class A{
    public int a;
    public int b;
    public A(int a, int b){
        this.a = a;
        this.b = b;
    }
}