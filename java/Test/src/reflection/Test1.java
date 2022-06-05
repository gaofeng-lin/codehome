package com.gaofeng.reflection;


import java.io.InputStream;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Properties;



public class Test1 {
        public static void main(String[] args) throws Exception {
            /**
             * 前提：不能改变该类的任何代码。可以创建任意类的对象，可以执行任意方法
             */
            //1.加载配置文件
            //1.1创建Properties对象
            Properties properties = new Properties();
            //1.2加载配置文件，转换为一个集合
            //1.2.1获取class目录下的配置文件  使用类加载器
            ClassLoader classLoader = com.gaofeng.reflection.Test1.class.getClassLoader();
            InputStream resourceAsStream = classLoader.getResourceAsStream("pro.properties");
            properties.load(resourceAsStream);
            //2.获取配置文件中定义的数据
            String className = properties.getProperty("className");
            String methodName = properties.getProperty("methodName");

            //加载类到内存中
            Class<?> aClass = Class.forName(className);
            //创建对象
            Object o = aClass.newInstance();
            //获取对象方法
            Method method = aClass.getMethod(methodName);
            //执行方法
            method.invoke(o);

        }
    }




