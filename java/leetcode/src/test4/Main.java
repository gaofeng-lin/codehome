//package test4;
//
//import java.util.*;
//
//import static java.util.Collections.*;
//
//public class Main {
//
//    private static HashMap<String,Integer> total_map = new HashMap<>();
//    private static HashMap<String,Integer> hot_map = new HashMap<>();
//    private static HashMap<String,Integer> font_end_map = new HashMap<>();
//
//
//    public static String cmp_hot(ArrayList<String> tmp_list,HashMap<String,Integer> hot_map){
//        return " ";
//    }
//
//    public static String cmp_title_first(String[] s){
//        return " ";
//    }
//
//    public static String cmp_file_first(String[] s){
//        return " ";
//    }
//
//    public static void main(String[] args){
//
//        Scanner sc = new Scanner(System.in);
//
//        String s_tr = sc.nextLine();
//        int top_num = Integer.parseInt(s_tr.split(" ")[0]);
//        int file_num = Integer.parseInt(s_tr.split(" ")[1]);
//
//        int count=1;
//
//        for(int i=1;i<2*file_num+1;i++){
//            String try1 = sc.nextLine();
//
//            String[] s = try1.split(" ");
//            for(String s1:s){
//                if(total_map.containsKey(s1)){
//                    if(i%2==0){
//                        total_map.compute(s1,(key,value)->value+1);
//                    }
//                    else {
//                        total_map.compute(s1,(key,value)->value+3);
//                        hot_map.compute(s1,(key,value)->value+3);
//                    }
//                }
//                else {
//                    if(i%2==0){
//                        total_map.put(s1,1);
//                        font_end_map.put(s1,count);
//                        count++;
//                    }
//                    else {
//                        total_map.put(s1,3);
//                        hot_map.put(s1,3);
//                        font_end_map.put(s1,count);
//                        count++;
//                    }
//                }
//            }
//       }
////        排序函数
////        Set<Map.Entry<String, Integer>> entrySet = map.entrySet();
//        List<Map.Entry<String, Integer>> total_list = new ArrayList<>(total_map.entrySet());
//        sort(total_list, new Comparator<Map.Entry<String, Integer>>() {
//            @Override
//            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
//                return o2.getValue()-o1.getValue();
//            }
//        });
//
//        List<Map.Entry<String, Integer>> hot_list = new ArrayList<>(hot_map.entrySet());
//        sort(hot_list, new Comparator<Map.Entry<String, Integer>>() {
//            @Override
//            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
//                return o2.getValue()-o1.getValue();
//            }
//        });
//
//        List<Map.Entry<String, Integer>> font_end_list = new ArrayList<>(font_end_map.entrySet());
//        sort(font_end_list, new Comparator<Map.Entry<String, Integer>>() {
//            @Override
//            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
//                return o1.getValue()-o2.getValue();
//            }
//        });
//
//
////        System.out.println(total_list);
////        System.out.println(hot_list);
////        System.out.println(font_end_list);
//
////        那几个数的值
//        int tmp_top_num=top_num;
//        HashSet<Integer> set = new HashSet<>();
//        for (Map.Entry s :total_list){
//
//            if((!set.contains((Integer) s.getValue()))&&(top_num>0)){
//                set.add((Integer) s.getValue());
//                top_num--;
//            }
//
//        }
//        List<Integer> myList = new ArrayList<>(set);
//        Collections.sort(myList,Collections.reverseOrder());
//
//        int k=0;
//        ArrayList<String> tmp_list = new ArrayList<>();
//
//        for(int i:myList){
//            if(top_num>0){
//                for(int j=0;j<total_list.size();j++){
//                    if(total_list.get(j).getValue()==i){
//                        tmp_list.add(total_list.get(j).getKey());
//                    }
//                }
//                if(tmp_list.size()==1){
//                    System.out.println(tmp_list.get(0));
//                    System.out.println(" ");
//                }
//                else {
//                    String res=cmp_hot(tmp_list,hot_map);
//                    System.out.println(res);
//                    System.out.println(" ");
//                }
//                top_num--;
//                tmp_list.removeAll();
//            }
//        }
//
////        for(int i=0;i<total_list.size();i++){
////            if(myList.get(k)==total_list.get(i).getValue()){
////                tmp_list.add(total_list.get(i).getKey());
////            }
////            else {
////                k++;
////                top_num--;
////                i--;
////                if(tmp_list.size()==1){
////                    System.out.println(tmp_list.get(0));
////                    System.out.println(" ");
////                }
////                else {
////
////                }
////            }
////        }
//
////        ArrayList<String> s_tmp = new ArrayList<>();
////        for(int i=0;i<list.size()-1;i++){
////            if (top_num>0){
////                if(list.get(i).getValue()!=list.get(i+1).getValue()){
////                    System.out.println(list.get(i).getKey());
////                    top_num--;
////                }
////                else {
//////                    s_tmp.add(list.get(i).getKey());
//////                    s_tmp.add(list.get(i+1).getKey());
//////                    while(list.get(i).getValue()!=list.get(i+1).getValue()){
//////                        i++;
//////                        s_tmp.add(list.get(i+1).getKey());
//////                    }
//////                    System.out.println(s_tmp);
////                }
////            }
////
////        }
////        HashSet<Integer> set = new HashSet<>();
////        for (Map.Entry s :list){
////
////            if((!set.contains((Integer) s.getValue()))&&(top_num>0)){
////                set.add((Integer) s.getValue());
////                top_num--;
////            }
////
////        }
////        set.remove(0);
////        System.out.println(set);
//
////        map.remove("");
////        System.out.println(map);
//    }
//}