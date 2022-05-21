package ReentrantLock;

import java.util.concurrent.locks.ReentrantReadWriteLock;

//ReentrantReadWriteLock读锁共享
public class Demo2 {
    private ReentrantReadWriteLock lock = new ReentrantReadWriteLock();
    private int i;

    public String readI(){
        lock.readLock().lock();
        System.out.println(Thread.currentThread().getName()+"占用锁, i->" + i);
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            System.out.println(Thread.currentThread().getName()+"释放锁, i->" + i);
            lock.readLock().unlock();
        }
        return i + "";
    }

    public static void main(String[] args) {
        final Demo2 demo2 = new Demo2();
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                demo2.readI();
            }
        };
        new Thread(runnable, "t1").start();
        new Thread(runnable, "t2").start();
        new Thread(runnable, "t3").start();
    }
}