package org.example;

/**
 * Hello world!
 *
 */
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class App {
    private static final Log LOGGER = LogFactory.getLog(App.class);
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");
//        HelloWorld obj = context.getBean("helloWorld",HelloWorld.class);
        Student obj = context.getBean("student", Student.class);
//        obj.getMessage();
        LOGGER.info(obj.toString());

    }
}
