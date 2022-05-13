#coding=UTF-8

# 生成最初版本的表格，包含所有的变量

import xml.dom.minidom
import re,os

list=['a', 'b', 'str_scheme_name', 'str_limiter']
doc = xml.dom.minidom.Document() 
root = doc.createElement('version-check')
doc.appendChild(root)

for i in list:
    var_name = doc.createElement(i)

    version=doc.createElement('version')
    version.setAttribute('v','100')
    version.appendChild(doc.createTextNode(i))

    # version_name=doc.createElement('name')
    # version_name.appendChild(doc.createTextNode(i))

    # version.appendChild(version_name)

    var_name.appendChild(version)
    # nodeManager.setAttribute('version','303')

    # nodeName=doc.createElement('name')

    root.appendChild(var_name)



fp = open('C:/Users/76585/Desktop/shell/cfdname2/tow.xml', 'w')
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


# def get_bianliang(file_path):
 
#     list=[]
#     f=open(file_path)
#     line=f.readline()
#     while line:
#                 # new_line=re.split(r'(;, ,\t,=,\n)\s',str(line))
#         new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
       
#         for i in new_line:
#             if i=='':
#                 new_line.remove(i)
                
#             if len(new_line)==3:
#                 list.append(new_line[1])
                
#         line=f.readline()
#     return list



# if __name__ == '__main__':
  
#     list1=[]
#     # list2=[]
#     list1=get_bianliang('C:/Users/76585/Desktop/shell/cfdname2/cfd_para.353')
#     # list2=get_bianliang('C:/Users/76585/Desktop/shell/cfdname2/cfd_para.354')

#     print list1


  