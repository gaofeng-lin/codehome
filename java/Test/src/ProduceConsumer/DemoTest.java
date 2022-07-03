package ProduceConsumer;

public class DemoTest {

    public static void main(String[] args) {
        ProductFactory productFactory = new ProductFactory();

        new Thread(new Producer(productFactory), "1号生产者").start();
        new Thread(new Producer(productFactory), "2号生产者").start();
        new Thread(new Producer(productFactory), "3号生产者").start();
        new Thread(new Consumer(productFactory), "1号消费者").start();
        new Thread(new Consumer(productFactory), "2号消费者").start();
    }
}