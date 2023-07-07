#coding=UTF-8

# 在4的基础上，修改判别条件。把相同的变量按a1,a2,a3顺序命名。如果相邻两个之间有未命名的，比较数量，数量相同，改名。
# 一方全为0，增加或修改。其余的人工处理

import re
import os
import json,copy
import sys
from collections import Counter

def get_value_name_and_value(file_path):
    
    # 提取第一个版本的版本号
    version_name=draw_version(file_path)
    dict={}
    f=open(file_path)
    line=f.readline()

    while line:
        tmp=line[:2]
        if tmp == '//' :
            line=f.readline()
            continue


        if line.find('*')!=-1:
            line=f.readline()
            continue

        if line.find('#')!=-1:
            line=f.readline()
            continue

        # new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
        new_line=re.split(r';',str(line))
        new_line1=re.split(r'=',str(new_line[0]))
        # print(new_line1)
        if len(new_line1)==2:
         

            new_line_name=re.split(r'[\t,\s]\s*',new_line1[0])
            # print(new_line_name[1])

            new_line_value_num=re.split(r'[;]',new_line1[1])
            # print(new_line_value_num[0].strip())

            dict[new_line_name[1]]=new_line_value_num[0].strip()
            # list1.append(new_line_name[1])
          
        line=f.readline()
    f.close()
    return dict

def draw_version(file_path):
    new_line=re.split(r'[/]',str(file_path))
    new_line=new_line[-1]
    version_name=re.sub('\D','',new_line)
    return version_name

if __name__=='__main__':
    old_version_list=get_value_name_and_value('C:/Users/Administrator/Desktop/try1/cfd_para_5389.txt')    

    print(len(old_version_list))
    #  print(len(list(set(old_version_list))))
    # print(Counter(old_version_list))
    # myset=set(old_version_list)
    # for i in myset:
    #     print("%d found %d" %(i,myset.count(i)))