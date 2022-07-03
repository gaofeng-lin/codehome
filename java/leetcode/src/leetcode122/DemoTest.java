package leetcode122;
//给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

//在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
//
//        返回 你能获得的 最大 利润 。

public class DemoTest {


    public static int maxProfit(int[] prices) {
        if(prices==null || prices.length==0) {
            return 0;
        }
        return dfs(prices,0,false,2);
    }

    private static int dfs(int[] prices, int index, boolean status, int count) {
        if(index==prices.length || count == 0) {
            return 0;
        }
        //定义三个变量，分别记录[不动]、[买]、[卖]
        int a=0,b=0,c=0;
        a = dfs(prices,index+1,status, count);
        if(status)  {
            //递归处理卖的情况
            count = count - 1;
            b = dfs(prices,index+1,false, count)+prices[index];
            count = count + 1;
        } else {
            //递归处理买的情况
            count = count - 1;
            c = dfs(prices,index+1,true, count)-prices[index];
            count = count + 1;
        }
        //最终结果就是三个变量中的最大值
        return Math.max(Math.max(a,b),c);
    }
    public static void main(String[] args) {
//        System.out.println("hello");
        int[] input = {7, 1, 5, 3, 6, 4};
//        int[] input = {5, 3, 6};
        int fin = maxProfit(input);
        System.out.println(fin);
    }
}