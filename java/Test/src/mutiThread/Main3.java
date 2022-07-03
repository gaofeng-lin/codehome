package mutiThread;


//import java.util.Objects;



public class Main3 {
    private static Object resa = new Object();
    private static Object resb = new Object();

    public static void main(String[] args) {
        Thread ta = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (resa){
                    System.out.println(Thread.currentThread().getName()+"获取A资源");
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread().getName()+"开始申请B");
                    synchronized (resb){
                        System.out.println(Thread.currentThread().getName()+"获取B资源");
                    }
                }
            }
        });

        Thread tb = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (resa){
                    System.out.println(Thread.currentThread().getName()+"获取A资源");
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread().getName()+"开始申请B");
                    synchronized (resb){
                        System.out.println(Thread.currentThread().getName()+"获取B资源");
                    }
                }
            }
        });

        ta.start();
        tb.start();
    }
}