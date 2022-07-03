package Decorator;

import com.sun.org.apache.xpath.internal.SourceTree;

public class Rectangle implements Shape {

    @Override
    public void draw() {
        System.out.println("shape: Rectangle");
    }
}