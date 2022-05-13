#coding=UTF-8

# 版本对比可能出现改名字的情况，单独为这个版本生成一个标签，后续出现这个情况也是放在这里面。人工来校验是否改了变量名

list1=['a', 'mgrid', 'b', 'str_scheme_name', 'str_limiter', 'masterfilename']
list2=['a', 'mgrid', 'b1', 'str_scheme_name','ok', 'str_limiter', 'masterfilename']

b=[i for i in list2 if i  in list1]


list3=list(set(list1)-set(b))
list4=list(set(list2)-set(b))

dict1={}
dict2={}


# if len(list1)==len(list2) and len(list1)==0:
#     print 'same'

# if (len(list1)==0 or len(list2)==0) and len(list2) !=0:
#     print 'add nodes' 

if len(list3)!=0 and len(list4)!=0:
    print 'add tag'

    # 记录索引
    
    for i in list3:
        dict1[list1.index(i)]=i

    for i in list4:
        dict2[list2.index(i)]=i
    
    print dict1,dict2
