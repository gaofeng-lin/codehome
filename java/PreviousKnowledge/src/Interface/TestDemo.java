package Interface;

public class TestDemo {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.eat();

        Animal fakecat = new Dog();
        fakecat.eat();
    }
}