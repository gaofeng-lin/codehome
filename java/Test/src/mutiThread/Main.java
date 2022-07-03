package mutiThread;


class TreadRunable implements Runnable{
    @Override
    public void run() {
        System.out.println("线程"+Thread.currentThread()+"正在执行");
    }
}

public class Main {


    public static void main(String[] args) throws InterruptedException {
//        new Thread(new TreadRunable()).start();
        Thread t1 = new Thread(new TreadRunable());
        t1.setName("one");

        Thread t2 = new Thread(new TreadRunable());
        t2.setName("two");

        t1.start();
        t1.sleep(5000);

        t2.start();
        t2.sleep(1000);

        System.out.println("end");
    }
}