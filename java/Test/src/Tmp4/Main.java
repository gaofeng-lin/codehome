package Tmp4;

import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[][] num = new int[2][2];

        for(int i=0;i<2;i++){
            String s = sc.nextLine();
            int j=0;
           for (char c:s.toCharArray()){
                num[i][j] = c-'0';
               j++;
           }
        }
        System.out.println(num[0][1]);
    }

}