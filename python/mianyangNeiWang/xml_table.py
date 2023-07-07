#coding=UTF-8
#生成版本对比表格

import xml.dom.minidom
import re
import os
import xml.etree.ElementTree as ET

def get_bianliang(file_path):
    
    list=[]
    f=open(file_path)
    line=f.readline()

    while line:
        
        if line.find('//')!=-1:
            line=f.readline()
            continue

        if line.find('*')!=-1:
            line=f.readline()
            continue

        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))

        for i in new_line:
            if i == '':
                new_line.remove(i)

            if len(new_line)==3:
                list.append(new_line[1])
        
        line=f.readline()
    return list

def init_table(init_path):
    
    list=get_bianliang(init_path)
    doc=xml.dom.minidom.Document()
    root=doc.createElement('version-check')
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
    
    fp=open('C:/Users/Administrator/Desktop/cfd_version/all_version.xml','wb')
    doc.writexml(fp,indent='\t',addindent='\t',newl='\n',encoding="utf-8")


def compare(old_path,new_path):
    list1=get_bianliang(old_path)
    list2=get_bianliang(new_path)

    b=[x for x in list2 if x not in list1]

    

    new_line=re.split(r'[/]',str(new_path))
    new_line=new_line[-1]
    end=re.sub('\D','',new_line)

    tree=ET.parse('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')
    root=tree.getroot()

    for i in b:
        newnode=ET.Element(i)

        version=ET.Element('version')
        version.attrib={'v':end}
        version.text=i

        # version_name=ET.Element('name')
        # version_name.text=i

        # version.append(version_name)
        newnode.append(version)
        root.append(newnode)
    
    tree.write('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')


if __name__ == '__main__':
    # list=[]
    # list=get_bianliang('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_304.txt')

    # print list
    init_table('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_304.txt')

    compare('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_353.txt','C:/Users/Administrator/Desktop/cfdnames2/cfd_para_354.txt')

    # list=compare('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_353.txt','C:/Users/Administrator/Desktop/cfdnames2/cfd_para_354.txt')
    # print list