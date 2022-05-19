package ProduceConsumer;

import java.util.LinkedList;

public class ProductFactory {
    private LinkedList<String> products;
    private int capacity = 10;
    public ProductFactory(){
        products = new LinkedList<>();
    }

//    生成方法
    public synchronized void produce(String product){
        while(capacity == products.size()){
            System.out.println("线程"+Thread.currentThread().getName()+"准备生成，但是仓库满了");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        products.add(product);

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("线程"+Thread.currentThread().getName()+"生成完毕，当前剩余" + products.size());
        notify();
    }

//    消费者方法
    public synchronized String consume(){
        while(products.size() == 0){
            System.out.println("线程"+Thread.currentThread().getName()+"准备消费，但是没有商品了");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        String product = products.remove(0);

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("线程"+Thread.currentThread().getName()+"消费了一件商品，当前剩余" + products.size());
        notify();

        return product;
    }
}