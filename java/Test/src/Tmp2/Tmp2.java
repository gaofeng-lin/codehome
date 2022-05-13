package Tmp2;

import java.util.Scanner;
import java.util.*;

public class Tmp2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int dig_ip = sc.nextInt();

        StringBuilder res = new StringBuilder();

        int tmp;
        int k=1;
        while(dig_ip!=0){
            tmp = (int) (dig_ip%Math.pow(2,k*8));
            res.append(tmp);
            dig_ip=dig_ip-(int)(tmp*Math.pow(2,(k-1)*8));
            k++;
        }
        System.out.println(res);


//        ip转10进制
//        String ip = sc.nextLine();
//
//        String[] s = ip.split("\\.");
//
//        ArrayList<Integer> list = new ArrayList<>();
//        int sum=0;
//        int k=0;
//        for(int i=s.length-1;i>=0;i--){
//            int tmp = Integer.parseInt(String.valueOf(s[i]));
//            sum+=tmp*Math.pow(2,k);
//            k+=8;
//        }
//        System.out.println(sum);
    }

}