package Dfs;

import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Tmp1 {

    private static List<int[]> path = new ArrayList<int []>();
    private static List<int[]> res = new ArrayList<int []>();

    public static void dfs(int[][] maze,int i,int j){
        if (i<0||j<0||i>maze.length||j>maze[0].length||maze[i][j]==1){
            return;
        }
        else {
            path.add(new int[]{i,j});
            maze[i][j] = 1;

            dfs(maze,i+1,j);
            dfs(maze,i-1,j);
            dfs(maze,i,j+1);
            dfs(maze,i,j-1);
            path.remove(path.size()-1);
            maze[i][j]=0;
        }
    }

    public static void main(String[] args){
//        1.处理输入
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
//        2.生成矩阵
        int[][] maze = new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                maze[i][j] = sc.nextInt();
            }
        }

//        3.调用函数生成结果
        dfs(maze,0,0);
        for(int [] s:res){
            System.out.println("("+s[0]+","+s[1]+")");
        }
    }
}