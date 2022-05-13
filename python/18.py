#coding=UTF-8

# 在比较函数中添加新的功能，新增变量使用add_nodes函数。可能改名使用add_tag函数


import os,re
import xml.dom.minidom
import xml.etree.ElementTree as ET
# 迭代读取文件，更新表格

# 1.生成初始表格
def init_table(init_path):
    list=get_bianliang(init_path)
    doc = xml.dom.minidom.Document() 
    root = doc.createElement('version-check')
    doc.appendChild(root)

    # manual_check=doc.createElement('manual_check')
    # root.appendChild(manual_check)

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


# 通过传入文件的路径，获取文件的变量名并存储在列表里面，最后返回一个列表
def get_bianliang(file_path):
    # dict={}
    list=[]
    f=open(file_path)
    line=f.readline()
    while line:

        if line.find('//')!=-1:
            line=f.readline()
            continue
                
        if line.find('#')!=-1:
            line=f.readline()
            continue

        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
        
        for i in new_line:
            if i=='':
                new_line.remove(i)
                
            if len(new_line)==3:
                list.append(new_line[1])
                
            
        line=f.readline()

    f.close()
    return list


# list表示要添加的变量名，end表示版本号
def add_nodes(list,end):

    
    tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')
    root=tree.getroot()
    for i in list:
        newnode=ET.Element(i)
        version=ET.Element('version')
        version.attrib={"v":end}
        version.text=i
        newnode.append(version)
        # newnode.text=end  
        root.append(newnode)   
    tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')


def add_tag():
    
    return 0

def compare(file_path):

    file_list=os.listdir(file_path)
    file_list.sort(key=lambda x:int(x[9:-4]))
    

    for i in range(0,len(file_list),1):
        l1=file_list[i:i+2]
        if len(l1)==2:
            
            list1=get_bianliang(file_path+'/'+l1[0])
            list2=get_bianliang(file_path+'/'+l1[1])

            # 共有元素
            a=[i for i in list2 if i  in list1]

            # 除去共有元素，各自独有的元素
            list3=list(set(list1)-set(a))
            list4=list(set(list2)-set(a))

            if len(list3)==len(list4) and len(list3)==0:
                break

            if (len(list3)==0 or len(list4)==0) and len(list4) !=0:
                print 'add nodes' 
                new_line=re.split(r'[/]',str(file_path+'/'+l1[1]))
                new_line=new_line[-1]
                # re.sub是 替换函数，将非数字替换为空格
                end=re.sub('\D','',new_line)
                add_nodes(list4,end)

            if len(list3)!=0 and len(list4)!=0:
                print 'add tag'

            

            # tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')
            # root=tree.getroot()

            # for i in b:
            #     newnode=ET.Element(i)

            #     version=ET.Element('version')
            #     version.attrib={"v":end}
            #     version.text=i


            #     newnode.append(version)
            #     # newnode.text=end  
            #     root.append(newnode)    

            # tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')


if __name__ == '__main__':

    init_table('C:/Users/76585/Desktop/cfdname1/cfd_para_304.txt')

    compare('C:/Users/76585/Desktop/cfdname1')
