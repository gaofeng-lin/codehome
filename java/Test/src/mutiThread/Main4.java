package mutiThread;

public class Main4 implements Runnable {
    @Override
    public void run() {
        try {
            testBlock();
        } catch (InterruptedException e) {

        }

    }

    public static void main(String[] args) {
        Thread t1 = new Thread(new Main4());
        t1.setName("T-one");

        Thread t2 = new Thread(new Main4());
        t2.setName("T-two");

        t1.start();
        t2.start();
    }

    public  synchronized void testBlock() throws InterruptedException {
        System.out.println("线程"+Thread.currentThread().getName()+"进来了");
        this.wait();
        System.out.println("线程"+Thread.currentThread().getName()+"执行，其它排队");
    }
}