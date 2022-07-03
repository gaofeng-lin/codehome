package Sort;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Student {
    private String name;
    private int age;
    private int money;
    private int height;

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public int getMoney() {
        return money;
    }

    public int getHeight() {
        return height;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setMoney(int money) {
        this.money = money;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    Student(String name, int age, int money, int height) {
        this.name = name;
        this.age = age;
        this.money =money;

        this.height = height;
    }
}

/**
 * @ 排序规则，按照年龄排序，若年龄相同，按照工资排序，若工资相同，按照身高排序

 *
 */
public class DemoTest {

    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        students.add(new Student("zhangshan", 21, 3000, 180));
        students.add(new Student("zhcngsan",27,4000,180));
        students.add(new Student("zhangsan",15,1000,180));
        students.add(new Student("zhangsan",21,5000,180));
        students.add(new Student("zhangsan",45,4000,180));
        students.add(new Student("zhangsan",21,5000,174));
        students.add(new Student("zhangsan",20,4000,180));
        students.add(new Student("zhangsan",33,4000,180));
        students.add(new Student("adobe",45,4000,180));
        students.add(new Student("tom",45,4000,180));
        students.add(new Student("zhangsan",99,4000,180));
        students.add(new Student("zhangsan",21,5000,160));

        Collections.sort(students, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                int x = o1.getAge() - o2.getAge();
                int y = o1.getMoney() - o2.getMoney();
                int z = o1.getHeight() - o2.getHeight();

                if(x == 0) {
                    if(y == 0) {
                        if(z == 0) {
                            return o1.getName().compareTo(o2.getName());
                        }
                            return z;
                    }
                        return y;
                }
                    return x;
            }
        });
        System.out.println("姓名" + "\t" + "\t" + "年龄" + "\t" + "工资" + "\t" + "身高" );
        for(Student s : students) {
            System.out.println(s.getName()+ "\t" + s.getAge() + "\t" + s.getMoney() + "\t" + s.getHeight());
        }

    }



}