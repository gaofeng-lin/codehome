package Tmp12;


import java.util.Arrays;
import java.util.Scanner;

//此题暴力求解
//0表示进攻，1表示防守
//左边是进攻，右边是防守；W是左边，V是右边

public class Main {

    public static int compute_socer(String w, String v){
        int socer_w = 0;
        int socer_v = 0;
        int len = w.length();
        char[] tmp_w = w.toCharArray();
        char[] tmp_v = v.toCharArray();
        for(int i=0;i<tmp_w.length;i++){
            if(tmp_w[i]=='0'){
                socer_w+=i+1;
            }
        }

        for(int i=0;i<tmp_v.length;i++){
            if(tmp_v[i]=='1'){
                socer_v+=i+1+len;
            }
        }
        return Math.abs(socer_v-socer_w);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        String str = sc.nextLine();
        char[] c = str.toCharArray();

        int min = Integer.MAX_VALUE;

        for(int i=0;i<c.length;i++){
//            先切割，切割好以后再计算
            char[] c1 = Arrays.copyOfRange(c,0,i+1);
            char[] c2 = Arrays.copyOfRange(c,i+1,c.length);
            String W = new String(c1);
            String V = new String(c2);
            int res = compute_socer(W,V);
            min = Math.min(min,res);

//            System.out.println(W);
//            System.out.println(V);
        }
        String tmp = new String(c);
        int last = compute_socer("",tmp);
        min = Math.min(last,min);

        System.out.println(min);

    }
}