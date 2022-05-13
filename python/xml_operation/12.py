#coding=UTF-8

# 对现有xml文件进行修改，添加新节点

# from xml.etree.ElementTree import ElementTree,Element
# import xml.dom.minidom

import xml.etree.ElementTree as ET

list1=['a', 'b', 'str_scheme_name', 'str_limiter']
list2=['a', 'mgrid', 'b', 'str_scheme_name', 'str_limiter']

# 新版本独有
b = [x for x in list2 if x not in list1]

tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')
root=tree.getroot()

for i in b:
    newnode=ET.Element(i)
    newnode.text='100'  
    root.append(newnode)    

tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')