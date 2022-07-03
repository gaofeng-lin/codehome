package test;

/**
 * Hello world!
 *
 */
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import test.controller.UserController;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
public class App {
    private static final Log LOGGER = LogFactory.getLog(App.class);
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");
        UserController userController = context.getBean("userController", UserController.class);
        userController.doStr();

    }
}
