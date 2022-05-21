package Condition;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DemoTest {
    public static void main(String[] args) {
        ProductFactor productFactor = new ProductFactor();
        new Thread(new Producer(productFactor), "1号生成者").start();
        new Thread(new Producer(productFactor), "2号生成者").start();
        new Thread(new Consumer(productFactor), "1号消费者").start();
        new Thread(new Consumer(productFactor), "2号消费者").start();
        new Thread(new Consumer(productFactor), "3号消费者").start();
    }
}

class ProductFactor{
    private LinkedList<String> products;
    private int capacity = 10;
    private Lock lock = new ReentrantLock();
    private Condition p = lock.newCondition();
    private Condition c = lock.newCondition();

    public ProductFactor(){
        products = new LinkedList<>();
    }

    public void produce(String product){
        try{
            lock.lock();
            while (capacity == products.size()){
                System.out.println(Thread.currentThread().getName()+"准备生成商品，但是仓库已经满了");
                try {
                    p.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            products.add(product);
            System.out.println(Thread.currentThread().getName()+"生成了一件商品，当前商品数量为" + products.size());
            c.signalAll();
        } finally {
            lock.unlock();
        }

    }

    public String consume(){
        try{
            lock.lock();
            while (products.size() == 0){
                System.out.println(Thread.currentThread().getName()+"准备消费商品，但是仓库为空");
                try {
                    c.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            String product = products.remove(0);
            System.out.println(Thread.currentThread().getName()+"消费了一件商品，当前商品数量为" + products.size());
            p.signalAll();
            return product;

        } finally {
            lock.unlock();
        }
    }
}

class Producer implements Runnable{

    private ProductFactor productFactor;
    public Producer(ProductFactor productFactor){
        this.productFactor = productFactor;
    }

    @Override
    public void run() {
        int i = 0;
        while(true){
            productFactor.produce(String.valueOf(i));

            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            i++;
        }
    }
}

class Consumer implements Runnable{
    private ProductFactor productFactor;
    public Consumer(ProductFactor productFactor){
        this.productFactor = productFactor;
    }

    @Override
    public void run() {
        while (true){
            productFactor.consume();
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}