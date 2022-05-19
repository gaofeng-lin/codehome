package ProduceConsumer;

public class Consumer implements Runnable {
    private ProductFactory productFactory;
    public Consumer(ProductFactory productFactory){
        this.productFactory = productFactory;
    }

    @Override
    public void run() {
        while (true){
            productFactory.consume();
        }
    }
}