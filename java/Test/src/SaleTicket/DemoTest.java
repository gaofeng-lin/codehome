package SaleTicket;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DemoTest {

    public static void main(String[] args) {
        TicketCenter ticketCenter = new TicketCenter();
        new Thread(new saleRollback(ticketCenter), "退票窗口").start();
        new Thread(new Consumer(ticketCenter), "1号窗口").start();
        new Thread(new Consumer(ticketCenter), "2号窗口").start();
    }
}

class TicketCenter {

    private int capacity = 10;
    private Lock lock = new ReentrantLock();
    private Condition saleLock = lock.newCondition();

    public void saleRollback() {
        try {
            lock.lock();
            capacity++;
            System.out.println(Thread.currentThread().getName()+ "正在退票,当前票数:" + capacity );
            saleLock.signalAll();
        } finally {
            lock.unlock();

        }
    }

    public void sale() {
        try {
            lock.lock();
            while (capacity == 0){
                try {
                    System.out.println(Thread.currentThread().getName() + "准备售票，但是没有票了");
                    saleLock.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            capacity--;
            System.out.println(Thread.currentThread().getName() + "卖出一张票，剩余：" + capacity + "张");
        } finally {
            lock.unlock();
        }
    }
}

class saleRollback implements Runnable {

    private TicketCenter ticketCenter = new TicketCenter();

    public saleRollback(TicketCenter ticketCenter) {
        this.ticketCenter = ticketCenter;

    }
    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            ticketCenter.saleRollback();
        }
    }
}

class Consumer implements Runnable {
     private TicketCenter ticketCenter = new TicketCenter();

    public Consumer(TicketCenter ticketCenter) {
        this.ticketCenter = ticketCenter;
    }

    @Override
    public void run() {
        while (true) {
            ticketCenter.sale();
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}