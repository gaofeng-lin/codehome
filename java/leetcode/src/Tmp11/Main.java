package Tmp11;

import java.util.ArrayList;

public class Main {

//    不是质数返回false
    public static boolean isZhishu(int num){
        boolean res = true;
        if(num>0){
            int k = (int) Math.sqrt(num);
            for(int i=2;i<=k;i++){
                if(num%i==0){
                    res = false;
                    break;
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int[] a={3,1,1,4,5,6};
        ArrayList<Integer>list = new ArrayList<>();
        for(int i=0;i<a.length;i++){
            list.add(a[i]);
        }

        while(list.size()!=1){
            for(int i=0;i<list.size();i++){
                int num = i+1;
//                不是质数返回false
                if(num==1||!isZhishu(num)){
                    list.set(i,-1);
                }
            }
            for(int i=0;i<list.size();i++){
                if(list.get(i)==-1){
                    list.remove(i);
                }
            }
        }
//        int[] res = new int[1];
//        res[0] = list.get(0);
        System.out.println(list.get(0));
    }
}