package Test;

import java.util.Arrays;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        String str = "aBDedcQW";

//        for (char c : str.toCharArray()) {
//            if(Character.isUpperCase(c)) {
//                System.out.println(c-'A');
//            }
//        }
        for (int i = 25; i >= 0; i--) {
            System.out.println((char)(i + 'A'));
        }

    }
}
