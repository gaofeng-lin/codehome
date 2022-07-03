package 四则运算;

import java.io.*;
import java.util.Stack;

public class Main{

    static int pos;
    public static int compute(String s){
        char ops = '+';
        int num = 0;
        Stack<Integer> val = new Stack<>();
        int temp;

        while(pos < s.length()){
            if(s.charAt(pos) == '{' || s.charAt(pos) == '[' || s.charAt(pos) == '('){
                pos++;
                num = compute(s);
            }

            while(pos < s.length() && Character.isDigit(s.charAt(pos))){
                num = num * 10 + s.charAt(pos) - '0';
                pos++;
            }

//            能走到这一步，说明charAt(pos)不是数字，只能是符号。
            switch (ops){
                case '+':
                    val.push(num);
//                    这个break跳出switch，继续下面的内容
                    break;
                case '-':
                    val.push(-num);
                    break;
                case '*':
                    temp = val.pop();
                    temp = temp * num;
                    val.push(temp);
                    break;
                case '/':
                    temp = val.pop();
                    temp = temp / num;
                    val.push(temp);
                    break;
            }
            num = 0;
            if(pos < s.length()) {
                ops = s.charAt(pos);
                if(s.charAt(pos) == '}' || s.charAt(pos) == ']' || s.charAt(pos) == ')'){
                    pos++;
//                  这个break会跳出while循环，进行下面的计算
                    break;
                }
            }
            pos++;
        }

        int sum = 0;
        while(!val.isEmpty()){
            sum += val.pop();
        }
        return sum;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        pos = 0;
        System.out.println(compute(str));
    }

}
