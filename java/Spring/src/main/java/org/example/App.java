package org.example;

/**
 * Hello world!
 *
 */
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.innerbean.Employee;
import org.innercollection.JavaCollection;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class App {
    private static final Log LOGGER = LogFactory.getLog(App.class);
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");
//        HelloWorld obj = context.getBean("helloWorld",HelloWorld.class);
//        Employee obj = context.getBean("employee", Employee.class);
        JavaCollection obj = context.getBean("javacollection", JavaCollection.class);
//        obj.getMessage();
        LOGGER.info(obj.toString());

    }
}
