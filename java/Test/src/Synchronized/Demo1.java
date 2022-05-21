package Synchronized;

//验证可重入锁
public class Demo1 {
    public static void main(String[] args) {
        new Thread(new SynTest()).start();
    }
}

class SynTest implements Runnable{

    public static void helloA(){
        System.out.println(Thread.currentThread().getName()+" helloA");
        helloB();
    }

    public static void helloB(){
        System.out.println(Thread.currentThread().getName()+" helloB");
    }

    @Override
    public void run() {
        helloA();
    }
}