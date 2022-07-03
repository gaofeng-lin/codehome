package Tmp4;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        int[][] arr1 = {{1, 2}, {3, 4}, {5, 6}};

        for (int i = 0; i < arr1.length; i++) {
            int[] tmp = arr1[i];
            System.out.println(Arrays.toString(tmp));
        }
    }

}