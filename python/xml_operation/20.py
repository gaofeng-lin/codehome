#coding=UTF-8

import os,re
import xml.dom.minidom
import xml.etree.ElementTree as ET
# 迭代读取文件，更新表格。判断文件夹内容为空



# 1.生成初始表格
def init_table(init_path):

    # 对文件夹里面的文件按版本号排序，找到第一个版本
    file_list=sort_list(init_path)
    if file_list==[]:
        return None
    path=init_path+'/'+file_list[0]

    version_num=draw_version(path)

    

    list=get_bianliang(path)
    # print list
    doc = xml.dom.minidom.Document() 
    root = doc.createElement('version-check')
    doc.appendChild(root)

    for i in list:
        var_name = doc.createElement(i)
     
        version=doc.createElement('version')
        version.setAttribute('v',version_num)
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


def sort_list(file_path):
    # 按照版本进行编号
    file_list=os.listdir(file_path)
    file_list.sort(key=lambda x:int(x[9:-4]))
    return file_list

def manual_check(new_version,list3,list4):

    tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')

    for i in list3:
        for j in list4:

            # 找到旧版本的节点
            tag1_name=tree.find(i)
 
        
            # 生成新版本节点
            # newnode1=ET.Element(j)

            version=ET.Element('version')
            version.attrib={"v":new_version,'needcheck':'true'}
            version.text=j

            # newnode1.append(version)

            tag1_name.append(version)

        tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')

def draw_version(file_path):
    new_line=re.split(r'[/]',str(file_path))
    new_line=new_line[-1]
    end=re.sub('\D','',new_line)
    return end

def compare(file_path):

    
    # file_list=os.listdir(file_path)
    # file_list.sort(key=lambda x:int(x[9:-4]))

    # 判断是否只有一个文件
    file_one=os.listdir(file_path)
    if len(file_one)==1:
        return
    
    # 按照版本进行编号
    file_list=sort_list(file_path)


    for i in range(0,len(file_list),1):
        l1=file_list[i:i+2]
        if len(l1)==2:
            
            list1=get_bianliang(file_path+'/'+l1[0])
            list2=get_bianliang(file_path+'/'+l1[1])

            # 两个版本共有变量
            b=[i for i in list2 if i  in list1]

            # 消除相同变量
            list3=list(set(list1)-set(b))
            list4=list(set(list2)-set(b))

            new_line=re.split(r'[/]',str(file_path+'/'+l1[1]))
            new_line=new_line[-1]
            # re.sub是 替换函数，将非数字替换为空格，end是版本号
            end=re.sub('\D','',new_line)
            
            if len(list3)!=0 and len(list4)!=0:
                manual_check(end,list3,list4)

            else:         
                # 新版本独有变量
                c=[i for i in list2 if i  not in list1]

                tree=ET.parse('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')
                root=tree.getroot()

                for i in c:
                    newnode=ET.Element(i)

                    version=ET.Element('version')
                    version.attrib={"v":end}
                    version.text=i


                    newnode.append(version)
                    # newnode.text=end  
                    root.append(newnode)    

                tree.write('C:/Users/76585/Desktop/shell/cfdname2/tow.xml')


if __name__ == '__main__':

    # init_table('C:/Users/76585/Desktop/cfdname1/cfd_para_304.txt')
    init_table('C:/Users/76585/Desktop/cfdname1')

    compare('C:/Users/76585/Desktop/cfdname1')
