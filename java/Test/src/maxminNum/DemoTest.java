package maxminNum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DemoTest {
    public static void main(String[] args) {
//        System.out.println("hello");
        int[] nums = {1, 2, 4, 6};
        int[][]operations = {{1,3}, {4,7}, {6,1}};
        int m = operations.length;
        int n = operations[0].length;

        ArrayList<Integer> list = new ArrayList<>();
        for(int j = 0; j < nums.length; j++) {
            list.add(nums[j]);
        }

        for(int i = 0; i < m; i++) {

            int index = list.indexOf(operations[i][0]);
            list.set(index, operations[i][1]);
        }

        int[] res = new int[list.size()];
        for(int k = 0; k < res.length; k++) {
            res[k] = list.get(k);
        }
//        list.toArray(new int[][]{res});
        System.out.println(res[0]);
//        return res;
    }

}
