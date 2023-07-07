#coding=UTF-8
#迭代读取文件，更新表格，判空,判断相似度

import xml.dom.minidom
import re
import os
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

def init_table(init_path):
    

    file_list=sort_version_list(init_path)
    if file_list==[]:
        return
    path=init_path+'/'+file_list[0]

    version_name=draw_version(path)

    list=get_value_name(path)
    doc=xml.dom.minidom.Document()
    root=doc.createElement('version-check')
    doc.appendChild(root)

    for i in list:
        var_name = doc.createElement(i)

        version=doc.createElement('version')
        version.setAttribute('v',version_name)
        version.appendChild(doc.createTextNode(i))

        # version_name=doc.createElement('name')
        # version_name.appendChild(doc.createTextNode(i))

        # version.appendChild(version_name)

        var_name.appendChild(version)

        root.appendChild(var_name)
    
    fp=open('C:/Users/Administrator/Desktop/cfd_version/all_version.xml','w')
    doc.writexml(fp,indent='\t',addindent='\t',newl='\n',encoding="utf-8")

def get_value_name(file_path):
    
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


def sort_version_list(file_path):

    file_list=os.listdir(file_path)
    file_list.sort(key=lambda x:int(x[9:-4]))
    return file_list

def manual_check(new_version_num,old_version_unique,new_version_unique):
    
    tree=ET.parse('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')

    for i in old_version_unique:
        for j in new_version_unique:

            if similarity(j,i) > 0.75:
                print 'change name'
                newnode=ET.Element(j)

                version=ET.Element('version')
                version.attrib={'v':new_version_num}
                version.text=j

                newnode.append(version)
                root.append(newnode)
            else:
                print

            # tag1_name=tree.find(i)

            # version=ET.Element('version')
            # version.attrib={'v':new_version_num,'needcheck':'true'}
            # version.text=j


            # tag1_name.append(version)
        
        tree.write('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')


# def manual_check(new_version,new_value_list):
    
#     tree=ET.parse('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')
#     root=tree.getroot()
    
#     for i in new_value_list:
#         newnode=ET.Element(i)

#         version=ET.Element('version')
#         version.attrib={'v':new_version,'needcheck':'true'}
#         version.text=i

#         newnode.append(version)
#         root.append(newnode)

#     tree.write('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')

def draw_version(file_path):
    new_line=re.split(r'[/]',str(file_path))
    new_line=new_line[-1]
    version_name=re.sub('\D','',new_line)
    return version_name

def similarity(a,b):
    return SequenceMatcher(None,a,b).ratio()

def compare(file_path):
    # old_version_list=get_value_name(old_path)
    # new_version_list=get_value_name(new_path)

    file_one=os.listdir(file_path)
    if len(file_one)==1:
        return
    
    file_list=sort_version_list(file_path)



    for i in range(len(file_list)):
        l1=file_list[i:i+2]
        if len(l1)==2:

            old_version_list=get_value_name(file_path+'/'+l1[0])
            new_version_list=get_value_name(file_path+'/'+l1[1])

            common_have=[i for i in new_version_list if i in old_version_list]

            old_version_unique=list(set(old_version_list)-set(common_have))
            new_version_unique=list(set(new_version_list)-set(common_have))

            new_line=re.split(r'[/]',str(file_path+'/'+l1[1]))
            new_line=new_line[-1]

            new_version_num=re.sub('\D','',new_line)

            if len(old_version_unique)!=0 and len(new_version_unique)!=0:
                # manual_check(end,list3,list4)
                manual_check(new_version_num,old_version_unique,new_version_unique)

            else:
                c=[i for i in new_version_list if i not in old_version_list]

                tree=ET.parse('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')
                root=tree.getroot()

                for i in c:
                    newnode=ET.Element(i)

                    version=ET.Element('version')
                    version.attrib={'v':new_version}
                    version.text=i

                    newnode.append(version)
                    root.append(newnode)

                tree.write('C:/Users/Administrator/Desktop/cfd_version/all_version.xml')


if __name__ == '__main__':
    # list=[]
    # list=get_value_name('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_304.txt')

    # print list
    # init_table('C:/Users/Administrator/Desktop/name_split2/Branch_Baka')

    # compare('C:/Users/Administrator/Desktop/name_split2/Branch_Baka')

    init_table('C:/Users/Administrator/Desktop/try1')
    compare('C:/Users/Administrator/Desktop/try1')
    # list=compare('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_353.txt','C:/Users/Administrator/Desktop/cfdnames2/cfd_para_354.txt')
    # print list