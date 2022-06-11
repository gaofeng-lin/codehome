package test.dao.impl;


import test.dao.UserDao;
import org.springframework.stereotype.Repository;

@Repository("userDao")
public class UserDaoImpl implements UserDao {
    @Override
    public void print() {
        System.out.println("C语言中文网");
    }
}
