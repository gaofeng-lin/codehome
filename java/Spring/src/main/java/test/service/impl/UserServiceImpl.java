package test.service.impl;

import test.dao.UserDao;
import test.service.UserService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

@Service("userService")
public class UserServiceImpl implements UserService {
    @Resource
    private UserDao userDao;

    public UserDao getUserDao() {
        return userDao;
    }


    @Override
    public void out() {
        userDao.print();
        System.out.println("一个精美的网站");
    }
}
