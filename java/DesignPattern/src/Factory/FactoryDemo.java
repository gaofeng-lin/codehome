package Factory;

public class FactoryDemo {

    public static void main(String[] args) {
        ShapeFactory shapeFactory = new ShapeFactory();
        Shape shape1 = shapeFactory.getshape("SQUARE");
        shape1.draw();

    }
}
