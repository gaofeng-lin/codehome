package 牛客_tmp;

import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();

        HashMap<String,Integer> map = new HashMap<>();
        map.put("english",0);
        map.put("space",0);
        map.put("digital",0);
        map.put("elsechar",0);
        char[] s = str.toCharArray();
        for(char c:s){
//            System.out.println(c);
            if(Character.isDigit(c)){
                map.compute("digital",(key,value)->value+1);
                continue;
            }
            if(c==' '){
                map.compute("space",(key,value)->value+1);
                continue;
            }
            if (Character.isLetter(c)){
                map.compute("english",(key,value)->value+1);
                continue;
            }
            else{
                map.compute("elsechar",(key,value)->value+1);
            }
        }
        System.out.println(map.get("english"));
        System.out.println(map.get("space"));
        System.out.println(map.get("digital"));
        System.out.println(map.get("elsechar"));
    }
}