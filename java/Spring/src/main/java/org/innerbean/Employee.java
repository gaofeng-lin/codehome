package org.innerbean;

public class Employee {
    //员工编号
    private String empNo;
    //员工姓名
    private String empName;
    //部门信息
    private Dept dept;
    public void setEmpNo(String empNo) {
        this.empNo = empNo;
    }
    public void setEmpName(String empName) {
        this.empName = empName;
    }
    public void setDept(Dept dept) {
        this.dept = dept;
    }
    @Override
    public String toString() {
        return "Employee{" +
                "empNo='" + empNo + '\'' +
                ", empName='" + empName + '\'' +
                ", dept=" + dept +
                '}';
    }
}
