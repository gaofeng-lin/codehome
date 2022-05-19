package mutiThread;

public class Main6 extends Thread {

    static int count = 0;

    public synchronized void increase() throws InterruptedException {
        System.out.println(Thread.currentThread().getName()+"获得锁");
        sleep(1000);
        count++;
        System.out.println(Thread.currentThread().getName()+" :"+count);
    }

    @Override
    public void run(){
        try {
            increase();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
        Main6 test = new Main6();
//        Main6 testNew = new Main6();
        Thread t1 = new Thread(test);

        Thread t2 = new Thread(test);

        t1.setName("thone");
        t2.setName("thtwo");

        t1.start();
        t2.start();

    }

}