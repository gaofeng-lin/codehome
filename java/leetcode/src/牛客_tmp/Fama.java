package 牛客_tmp;

import java.util.*;

public class Fama {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        HashSet<Integer> set = new HashSet<>();
        set.add(0);

        int[] w = new int[num];
        int[] nums = new int[num];

        for(int i=0;i<num;i++){
            w[i]=sc.nextInt();
        }

        for(int i=0;i<num;i++){
            nums[i]=sc.nextInt();
        }

        for(int i=0;i<num;i++){
            ArrayList<Integer> list = new ArrayList<>(set);
            for(int j=1;j<nums[i];j++){
                for (int k=0;k<list.size();k++){
                    set.add(list.get(k)+w[i]*j);
                }
            }
        }
        System.out.println(set.size());
    }
}
