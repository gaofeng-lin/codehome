package Tmp4;

import java.util.*;

public class Main {

    static class Student{

        private String name;

        private int  age;

        private int salary;

        private int height;
        Student(String name,int age,int salary,int height){

            this.name=name;
            this.age=age;
            this.salary=salary;
            this.height=height;

        }


        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public int getSalary() {
            return salary;
        }

        public void setSalary(int salary) {
            this.salary = salary;
        }

        public int getHeight() {
            return height;
        }

        public void setHeight(int height) {
            this.height = height;
        }




    }


    public static void main(String[] args){

//        Scanner sc = new Scanner(System.in);
//        int top_num = Integer.parseInt(sc.nextLine().split(" ")[0]);
//        int file_num = Integer.parseInt(sc.nextLine().split(" ")[1]);
        List<Student> students=new ArrayList<Student>();
        students.add(new Student("lin",21,3000,180));
        students.add(new Student("lin",27,4000,180));
        students.add(new Student("gao",15,1000,180));
        students.add(new Student("gao",21,5000,180));
        students.add(new Student("zhangsan",45,4000,180));
        students.add(new Student("zhangsan",21,5000,174));
        students.add(new Student("zhangsan",20,4000,180));
        students.add(new Student("zhangsan",33,4000,180));
        students.add(new Student("zhangsan",45,4000,180));
        students.add(new Student("zhangsan",76,4000,180));
        students.add(new Student("zhangsan",99,4000,180));
        students.add(new Student("zhangsan",21,5000,160));

        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                int x = o1.getAge() - o2.getAge();
                int y = o1.getSalary() - o2.getSalary();
                int z = o1.getHeight() - o2.getHeight();
                if(x==0){
                    if (y==0){
                        return z;
                    }
                    return y;
                }
                return x;
            }
        });
        for(Student s:students){
//            System.out.println(s.getName()+"\t"+s.getAge()+"\t"+s.getSalary());
            if (s.getName()=="lin"){
                System.out.println(s.getName()+"\t"+s.getSalary());
                s.setSalary(s.getSalary()+1000);
                System.out.println(s.getName()+"\t"+s.getSalary());
            }

        }


    }
}