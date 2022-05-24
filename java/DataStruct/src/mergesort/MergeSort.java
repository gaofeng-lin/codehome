package mergesort;

import java.util.Arrays;

public class MergeSort {

    public static void mergeSoft(int[] nums, int start, int end) {
        if(start >= end) return ;
        int mid = (start + end) / 2;
        if(mid > start) {
            mergeSoft(nums, start, mid);
        }
        if(end > mid+1) {
            mergeSoft(nums, mid+1, end);
        }

        int[] tmp = new int[end - start +1];

        int k = 0;
        int left = start;
        int right = mid + 1;
        while(left <= mid && right <=end) {
            if(nums[left] <= nums[right]) {
                tmp[k] = nums[left];
                left++;
            }else {
                tmp[k] = nums[right];
                right++;
            }
            k++;
        }

        while (left <= mid || right <=end) {
            if(left <= mid) {
                tmp[k] = nums[left];
                left++;
            }
            if(right <= end) {
                tmp[k] = nums[right];
                right++;
            }
            k++;
        }

        System.arraycopy(tmp, 0, nums, start, tmp.length);
    }

    public static void main(String[] args) {
        int[] data = {25, 5, 83, 99, 28, 57, 95, 57, 35, 3 };
        System.out.println("排序前：");

        System.out.println(Arrays.toString(data));

        System.out.println("开始排序");

        mergeSoft(data, 0, data.length - 1);

        System.out.println("排序后：");

        System.out.println(Arrays.toString(data));

    }
}