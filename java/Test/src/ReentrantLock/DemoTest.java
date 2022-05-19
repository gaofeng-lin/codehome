package ReentrantLock;

import java.util.concurrent.locks.ReentrantLock;

public class DemoTest {
    private static int count = 0;
    private static ReentrantLock lock = new ReentrantLock();

    public static void main(String[] args) {
        for (int i = 0; i < 2; i++){
            new Thread(new Runnable() {
                @Override
                public void run() {
                    for (int i = 0; i < 100; i++){
                        try{
                            lock.lock();
                            count++;
                        } finally {
                            lock.unlock();
                        }
                    }
                }
            }).start();
        }

        try{
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(count);
    }
}