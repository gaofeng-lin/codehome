package OptimisticLock;

import static java.lang.Thread.sleep;

public class Demo implements Runnable{
    private static int count = 0;

    @Override
    public void run() {
        try {
            sleep(10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        increase();
//        System.out.println(count);
    }

    public synchronized static void increase(){
        for (int i = 0; i < 100; i++){
                count++;
//            System.out.println(count);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread one = new Thread(new Demo(), "one");
        Thread two = new Thread(new Demo(), "two");
//        count++;
//        count++;
        one.start();
        two.start();
//        如果不加这一句，count的值输出还是0；因为线程还没来得及把值写回内存
        sleep(100);
        System.out.println(count);
    }
}