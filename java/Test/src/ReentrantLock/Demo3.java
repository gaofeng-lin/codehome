package ReentrantLock;

import java.util.concurrent.locks.ReentrantReadWriteLock;

//ReentrantReadWriteLock读锁共享
public class Demo3 {
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

    public void addI(){

        try{
            lock.writeLock().lock();
            System.out.println(Thread.currentThread().getName()+"占用锁, i->" + i);
            i++;
        } finally {
            System.out.println(Thread.currentThread().getName()+"释放锁, i->" + i);
            lock.writeLock().unlock();
        }

    }

    public static void main(String[] args) throws InterruptedException {
        final Demo3 demo3 = new Demo3();
        Runnable runnable1 = new Runnable() {
            @Override
            public void run() {
                demo3.readI();
            }
        };
        Runnable runnable2 = new Runnable() {
            @Override
            public void run() {
                demo3.addI();
            }
        };
        new Thread(runnable1, "t1").start();
        Thread.sleep(1000);
        new Thread(runnable2, "t2").start();
//        new Thread(runnable, "t3").start();

    }
}