package Tmp5;

import java.io.UnsupportedEncodingException;
import java.util.*;

public class Main {

    static class Football{
        private String name;
        private int points;
        private int goals_for;
        private int goals_against;
        private int goals_clean;

        Football(String name, int points, int goals_for, int goals_against, int goals_clean){
            this.name = name;
            this.points = points;
            this.goals_for = goals_for;
            this.goals_against = goals_against;
            this.goals_clean = goals_clean;
        }

        public String getName(){
            return name;
        }
        public void setName(String name){
            this.name = name;
        }

        public int getPoints(){
            return points;
        }
        public void setPoints(int i){
            this.points = i;
        }

        public int getGoals_for(){
            return goals_for;
        }
        public void setGoals_for(int i){
            this.goals_for = i;
        }

        public int getGoals_against(){
            return goals_against;
        }
        public void setGoals_against(int i){
            this.goals_against = i;
        }
        public int getGoals_clean(){
            return goals_clean;
        }
        public void setGoals_clean(int i){
            this.goals_clean = i;
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
//        测试数据
        int T = Integer.parseInt(sc.nextLine());




        for (int i=0;i<T;i++){
            List<Football> footballs = new ArrayList<>();
            int finsh=6;
            int last_game=3;
            while(finsh!=0){
                String[] line = sc.nextLine().split(" ");
                footballs.add(new Football(line[0],Integer.parseInt(line[1]),Integer.parseInt(line[2]),Integer.parseInt(line[3]),Integer.parseInt(line[2])-Integer.parseInt(line[3])));
                finsh--;
            }
//            现在要修改已有的数据
            while (last_game!=0){
                String[] line = sc.nextLine().split(" ");
                String name0 = line[0];
                String name1 = line[1];
                int goals_for1 = Integer.parseInt(line[2]);
                int goals_for2 = Integer.parseInt(line[3]);
                for(Football f:footballs){
                    if(f.getName().equals(name0)){
                        f.setGoals_for(f.getGoals_for()+goals_for1);
                        f.setGoals_clean(f.getGoals_for()-f.getGoals_against());
                        if(goals_for1>goals_for2){
                            f.setPoints(f.getPoints()+3);
                        }
                        if(goals_for1==goals_for2){
                            f.setPoints(f.getPoints()+1);
                        }

                        f.setGoals_against(f.getGoals_against()+(goals_for2));

                    }
                    if(f.getName().equals(name1)){
                        f.setGoals_for(f.getGoals_for()+goals_for2);
                        f.setGoals_clean(f.getGoals_for()-f.getGoals_against());
                        if(goals_for2>goals_for1){
                            f.setPoints(f.getPoints()+3);
                        }
                        if(goals_for1==goals_for2){
                            f.setPoints(f.getPoints()+1);
                        }

                        f.setGoals_against(f.getGoals_against()+(goals_for1));

                    }
                }
                last_game--;
            }
            Collections.sort(footballs, new Comparator<Football>() {
                @Override
                public int compare(Football o1, Football o2) {
                    int x = o2.getPoints()-o1.getPoints();
                    int y =o2.getGoals_clean()-o1.getGoals_clean();
                    int z = o2.getGoals_for()-o1.getGoals_for();

                    if(x==0){
                        if(y==0){
                            if(z==0){
                                return o1.getName().compareTo(o2.getName());
                            }
                            return z;
                        }
                        return y;
                    }
                    return x;
                }
            });
            for (Football f:footballs){
                System.out.println(f.getName()+" "+f.getPoints()+" "+f.getGoals_for()+" "+f.getGoals_against());
            }
            System.out.println("END");
        }


    }
}