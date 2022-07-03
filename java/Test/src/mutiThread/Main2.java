package mutiThread;
//
//public class Main2 implements Runnable {
//
//
//
//    @Override
//    public void run() {
//        Long start = System.currentTimeMillis();
//        int count = 0;
//        for (int i = 1; i <= 10000000; i++) {
//            count = count + i;
//        }
//        Long end = System.currentTimeMillis();
//        System.out.println("总执行时间： "+ (end-start) + " 毫秒, 结果 count = " + count);
//    }
//
//    public static void main(String[] args) {
//        Main2 to = new Main2(new Main2());
//        to.start();
//    }
//
//}


/**
 * 方式二：实现java.lang.Runnable接口
 */
public class Main2 implements Runnable{//步骤 1
    @Override
    public void run() {//步骤 2
        //run方法内为具体的逻辑实现
//        System.out.println("create thread by runnable implements");



    }
    public static void main(String[] args) {
        Thread one = new Thread(new Main2());
        one.start();
    }
}

