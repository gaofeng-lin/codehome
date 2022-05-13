package Test1;

import java.util.Scanner;
import java.lang.String;
import java.lang.Integer;
public class Test1{
    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
//        while(in.hasNext()){
            String[] temp=in.nextLine().split(" ");
            int sum=0;
            for(String s:temp)
                sum+=Integer.valueOf(s);
            System.out.println(sum);
//        }
    }
}
