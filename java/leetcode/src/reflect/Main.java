package reflect;

public class Main {
    public static void main(String[] args) {
        /**
         * 1、加载到内存，会产生一个类对应的 Class 对象
         * 2、链接，链接结束后 m = 0
         * 3、初始化
         <clint>() {
         System.out.println("A 类静态代码块初始化");
         m = 300;
         m = 100;
         }
         m = 100;
         */
        A a = new A();
        System.out.println(A.m);
    }
}

class A {

    static int m = 100;

    static {
        System.out.println("A 类静态代码块初始化");
        m = 300;
    }

//    static int m = 100;

    public A() {
        System.out.println("A 类的无参构造函数初始化");
    }
}
