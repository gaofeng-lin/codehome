package Tmp10;


//4-24腾讯


import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        char[][] c = new char[n][10000];
        int num_len=0;
//        sc.nextLine();

        for (int i=0;i<n;i++){
            String str = sc.nextLine();
            num_len = str.length();
            char[] c_tmp = str.toCharArray();
            for(int j=0;j<c_tmp.length;j++){
                c[i][j] = c_tmp[j];
            }
        }

//        现在矩阵为n*num_length的矩阵，按列来遍历
        ArrayList<Integer> list = new ArrayList<>();
        for(int j=0;j<num_len;j++){
            char[] tmp_c = new char[n];
            for(int i =0;i<n;i++){
                tmp_c[i] = c[i][j];
            }
            for (int i=0;i<n;i++){
                if(c[i][j]!='0'){

                    char[] res = Arrays.copyOfRange(tmp_c,i,n);
                    String s_list = new String(res);
                    list.add(Integer.valueOf(s_list));
                    break;
                }
            }

        }

//        把这些数去掉最前面的0，放入数组，用arrays.sort排序

        Collections.sort(list);
        System.out.println(list);
        StringBuilder sb = new StringBuilder();
        sb.append(list.get(0));
        for(int i=1;i<list.size();i++){
            sb.append(" "+list.get(i));
        }
        System.out.println(sb.toString());
    }
}