package mutiThread;

public class Main1 {
    public static void main(String[] args) throws InterruptedException {

        Thread tone = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(5000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("thread one sleep 5s");
            }
        });
        Thread ttwo = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("thread two sleep 10s");
            }
        });
        Thread tthree = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(8000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("thread three sleep 8s");
            }
        });

        long starttime = System.currentTimeMillis();
        tone.start();
        ttwo.start();
        tthree.start();
        System.out.println("执行完毕使用join方法");
        tone.join();
        ttwo.join();
        tthree.join();
        long endtime = System.currentTimeMillis();
        System.out.println("用时："+(endtime-starttime));
    }

}