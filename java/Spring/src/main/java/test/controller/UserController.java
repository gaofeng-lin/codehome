package test.controller;

import test.service.UserService;
import org.springframework.stereotype.Controller;

import javax.annotation.Resource;

@Controller("userController")
public class UserController {
    @Resource
    private UserService userService;

    public UserService getUserService() {
        return userService;
    }

    public void setUserService(UserService userService) {
        this.userService = userService;
    }

    public void doStr() {
        userService.out();
        System.out.println("专注于分享编程教程");
    }
}
