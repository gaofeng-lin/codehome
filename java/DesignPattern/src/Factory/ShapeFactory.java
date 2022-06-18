package Factory;

public class ShapeFactory {
    public Shape getshape(String ShapeType) {

        if (ShapeType.equalsIgnoreCase("SQUARE")) {
           return new Square();
        } else if (ShapeType.equalsIgnoreCase("RECTANGLE")) {
            return new Rectangle();
        }

        return null;
    }
}
