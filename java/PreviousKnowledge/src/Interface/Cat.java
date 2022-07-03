package Interface;

public class Cat implements Animal {
    @Override
    public void eat() {
        System.out.println("猫在吃东西");
    }

    @Override
    public void travel() {
        System.out.println("猫在旅游");
    }
}