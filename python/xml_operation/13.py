#coding=UTF-8

# 输入两个版本的路径，对比提取变化的变量名


import re,os
import xml.dom.minidom
import xml.etree.ElementTree as ET


def init_table(init_path):
    list=get_bianliang(init_path)
    doc = xml.dom.minidom.Document() 
    root = doc.createElement('version-check')
    doc.appendChild(root)

    for i in list:
        var_name = doc.createElement(i)

        version=doc.createElement('version')
        version.setAttribute('v','304')
        version.appendChild(doc.createTextNode(i))

        # version_name=doc.createElement('name')
        # version_name.appendChild(doc.createTextNode(i))

        # version.appendChild(version_name)

        var_name.appendChild(version)

        root.appendChild(var_name)

    fp = open('C:/Users/76585/Desktop/shell/cfdname2/tow.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

def get_bianliang(file_path):
    # dict={}
    list=[]
    f=open(file_path)
    line=f.readline()
    while line:
                
        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
        
        for i in new_line:
            if i=='':
                new_line.remove(i)
                
            if len(new_line)==3:
                list.append(new_line[1])
                
            
        line=f.readline()

    f.close()
    return list



def compare(old_path,new_path):
    list1=get_bianliang(old_path)
    list2=get_bianliang(new_path)
    # 新版本独有
    b = [x for x in list2 if x not in list1]

    new_line=re.split(r'[/]',str(new_path))
    new_line=new_line[-1]
    # re.sub是 替换函数，将非数字替换为空格
    end=re.sub('\D','',new_line)

    tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')
    root=tree.getroot()
    
    for i in b:
        newnode=ET.Element(i)

        version=ET.Element('version')
        version.attrib={"v":end}
        version.text=i

        # version_name=ET.Element('name')
        # version_name.text=i

        # version.append(version_name)

        newnode.append(version)
        # newnode.text=end  
        root.append(newnode)    

    tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')


if __name__ == '__main__':

    # 初始化表格
    # init_table('C:/Users/76585/Desktop/cfdname1/cfd_para_383.txt')

    # 迭代更新表格

    compare('C:/Tools/train_code/python/cfdname1/cfd_para_355.txt','C:/Tools/train_code/python/cfdname1/cfd_para_383.txt')