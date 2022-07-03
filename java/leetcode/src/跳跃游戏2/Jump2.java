package 跳跃游戏2;

//每次在上次能跳到的范围（end）内选择一个能跳的最远的位置（也就是能跳到max_far位置的点）作为下次的起跳点 ！

public class Jump2 {

    public static void main(String[] args){
        int[] nums={2,3,1,1,4,2,1};
        int res = jump(nums);
        System.out.println(res);
    }
    public static int jump(int[] nums) {
        int end = 0;// 上次跳跃可达范围右边界（下次的最右起跳点）
        int maxPosition = 0;// 目前能跳到的最远位置
        int steps = 0;// 跳跃次数
        for(int i = 0; i < nums.length - 1; i++){
            //找能跳的最远的
            maxPosition = Math.max(maxPosition, nums[i] + i);
            if( i == end){ //遇到边界，就更新边界，并且步数加一
                end = maxPosition;// 目前能跳到的最远位置变成了下次起跳位置的有边界
                steps++; // 进入下一次跳跃
            }
        }
        return steps;
    }

}