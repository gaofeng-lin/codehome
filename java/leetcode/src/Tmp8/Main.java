package Tmp8;

//4-20摩尔线程


//给定一个初始元素全部为0，大小为 m*n 的矩阵M以及在M上的一系列更新操作。
//        操作用二维数组表示，其中的每个操作用一个含有两个正整数a 和 b 的数组表示，
//        含义是将所有符合0 <= i < a 以及 0 <= j < b 的元素M[i][j]的值都增加 1。
//        在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
//
//        输入:
//        m = 3, n = 3
//        operations = [[2,2],[3,3]]
//        输出: 4

import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[][] list = {{2,2},{3,3}};
        int res = matrixOperate(3,3,list);
    }

    public static int matrixOperate(int m, int n,int[][] list){

        int[][] matrix = new int[m][n];

        for (int i=0;i<list.length;i++){
            for(int j=0;j<list[i][0];j++){
                for (int k=0;k<list[i][1];k++){
                    matrix[j][k]++;
                }
            }
        }

        int max=matrix[0][0];
        int count = 0;
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if(max==matrix[i][j]);
                count++;
            }
        }

        return count;


    }
}