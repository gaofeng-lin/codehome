package org.innercollection;


import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
public class Course {
    private static final Log LOGGER = LogFactory.getLog(Course.class);
    //课程编号
    private Integer courseId;
    //课程名称
    private String courseName;

    public void setCourseId(Integer courseId) {
        this.courseId = courseId;
    }

    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }

    @Override
    public String toString() {
        return "Course{" +
                "courseId=" + courseId +
                ", courseName='" + courseName + '\'' +
                '}';
    }
}
