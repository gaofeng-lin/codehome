package mutiThread;

import static java.lang.Thread.sleep;

public class Main5 {
    static int count = 0;

    public static synchronized void increse() throws InterruptedException {
        System.out.println(Thread.currentThread().getName()+"获得锁");
        sleep(1000);
        count++;
        System.out.println(Thread.currentThread().getName()+" :"+count);
    }


    public static void main(String[] args) {
        Thread to = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    increse();
                } catch (InterruptedException e) {
                }
            }
        });

        Thread tw = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    increse();
                } catch (InterruptedException e) {
                }
            }
        });

        to.setName("threadone");
        tw.setName("threadtwo");

        to.start();
        tw.start();
    }




}