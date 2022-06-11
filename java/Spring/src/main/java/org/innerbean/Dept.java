package org.innerbean;

public class Dept {
    //部门编号
    private String deptNo;
    //部门名称
    private String deptName;
    public void setDeptNo(String deptNo) {
        this.deptNo = deptNo;
    }
    public void setDeptName(String deptName) {
        this.deptName = deptName;
    }
    @Override
    public String toString() {
        return "Dept{" +
                "deptNo='" + deptNo + '\'' +
                ", deptName='" + deptName + '\'' +
                '}';
    }
}

