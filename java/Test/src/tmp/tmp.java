package tmp;

import java.lang.reflect.Array;
import java.util.*;
import java.lang.*;

import static sun.security.krb5.Config.getType;

public class tmp{

    public static int compute_sum(int num,ArrayList list1){
        int len = list1.size();

        int begin=num/2;
        int end=len-1-begin;
        int sum=0;
        for(;begin<=end;begin++){
            sum=sum+Integer.parseInt(String.valueOf(list1.get(begin)));
        }
        return sum;
    }

    public static void main(String[] args){
//
        Scanner sc = new Scanner(System.in);
        String input1 = sc.nextLine();
        int long1 = Integer.valueOf(input1);
        String[] input2 =   sc.nextLine().split(" ");
        ArrayList<Integer> list1 = new ArrayList<>();
        for(int i=0;i<input2.length;i++){
            list1.add(Integer.valueOf(input2[i]));
        }
        int tmp_l;
        if(long1%2==0){
            tmp_l=long1-1;
        }
        else{
            tmp_l=long1;
        }
        Collections.sort(list1);
        int i=1;
        int res=0;
        while(i<=tmp_l){
            int tmp=compute_sum(i,list1);
            res = res+tmp;
            i=i+2;
        }
        System.out.println(res);
    }
}