#coding=UTF-8

import os,re
import xml.dom.minidom
import xml.etree.ElementTree as ET

# 当出现变量改名的情况，增加新类型的标签

# 实现思路：将新版本所有变量都放在老版本变量的标签里面，标签属性包括新版本号，以及 needcheck这种标签，表示需要人工校验

list1=['a', 'mgrid', 'b', 'str_scheme_name', 'str_limiter', 'masterfilename']
list2=['a', 'mgrid', 'b1', 'str_scheme_name','ok', 'str_limiter', 'masterfilename']

b=[i for i in list2 if i  in list1]


list3=list(set(list1)-set(b))
list4=list(set(list2)-set(b))

print list3, list4

dict1={}
dict2={}

# if len(list3)!=0 and len(list4)!=0:
#     print 'add tag'
    # add_tag()

def add_tag():



    # # 假设新版本号是123
    end='123' 
    tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')

    for i in list3:
        for j in list4:

            # 找到旧版本的节点
            tag1_name=tree.find(i)
        
            # 生成新版本节点
            # newnode1=ET.Element(j)

            version=ET.Element('version')
            version.attrib={"v":end,'needcheck':'true'}
            version.text=j

            # newnode1.append(version)

            tag1_name.append(version)

        tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')



    # for i in list4:
    #     newnode=ET.Element(i)

    #     version=ET.Element('version')
    #     version.attrib={"v":end,'needcheck':'true'}


    #     version.text=i
    #     newnode.append(version)
    #     # newnode.text=end  
    #     root.append(newnode)  

    # tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')


if __name__ == '__main__':
    add_tag()