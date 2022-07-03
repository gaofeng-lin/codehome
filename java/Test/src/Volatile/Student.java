package Volatile;

public class Student {
    private String name;

    public synchronized String getName(){
        return name;
    }

    public synchronized void setName(String name){
        this.name = name;
    }

    public static void main(String[] args) {
        Thread one = new Thread(new Runnable() {
            @Override
            public void run() {
                Student student1 = new Student();
                student1.setName("1");
                System.out.println(student1.getName());
            }
        });
        Thread two = new Thread(new Runnable() {
            @Override
            public void run() {
                Student student2 = new Student();
                student2.setName("2");
                System.out.println(student2.getName());
            }
        });

        one.start();
        two.start();

    }
}