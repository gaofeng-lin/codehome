package ProduceConsumer;

public class Producer implements Runnable {
    private ProductFactory productFactory;
    public Producer(ProductFactory productFactory){
        this.productFactory = productFactory;
    }

    @Override
    public void run() {
        int i = 0;
        while(true){
            productFactory.produce(String.valueOf(i));
            i++;
        }
    }
}