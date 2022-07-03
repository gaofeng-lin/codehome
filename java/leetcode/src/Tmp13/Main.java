package Tmp13;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] str = sc.nextLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int m = Integer.parseInt(str[0]);



        int[] gupiao = new int[n];
        String[] s = sc.nextLine().split(" ");
        for(int i=0;i<n;i++){
            gupiao[i] = Integer.parseInt(s[i]);
        }
        int max = gupiao[0];
        m=m-gupiao[0];
        for(int i=1;i<n;i++){
            if(gupiao[i]>=gupiao[i-1]&&m>=gupiao[i]){
                max+=gupiao[i];
                m=m-gupiao[i];
            }
            if(gupiao[i]>=gupiao[i-1]&&m<gupiao[i]){
                max = max-gupiao[i];
                m=m+gupiao[i];
            }
        }
        System.out.println(max+m);

    }
}