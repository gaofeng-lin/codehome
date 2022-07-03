package offer13;

import java.util.Scanner;

public class offer13 {
    static int movingCount(int m, int n, int k) {
        int count=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int tmp1=check1(i);
                int tmp2=check1(j);
                if(tmp1+tmp2<=k){
                    count++;
                }
                else{
                    break;
                }
            }
        }
        return count;
    }

    static int check1(int x){
        if(x<=9){
            return x;
        }
        return x/10+x%10;
    }
    public static void main(String[] args){
//        System.out.print("hello");
//        int count=movingCount(16,8,4);
//        System.out.print(count);
        Scanner sc = new Scanner(System.in);
        String input1 = sc.nextLine();
        int long1 = Integer.valueOf(input1);
        int res = long1/2;
        System.out.println(res);

    }
}