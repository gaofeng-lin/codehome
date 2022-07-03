package Interface;

public class Dog implements Animal {

    @Override
    public void eat() {
        System.out.println("狗在吃东西");
    }

    @Override
    public void travel() {
        System.out.println("狗在旅游");
    }

}