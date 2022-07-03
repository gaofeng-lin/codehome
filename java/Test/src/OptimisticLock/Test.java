package OptimisticLock;



public class Test {

     private static int count = 0;

    public static void increase(){
        count++;
        count++;

    }
    public static void main(String[] args) {
        increase();
        System.out.println(count);
    }
}