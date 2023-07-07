#coding=UTF-8

import re
import os
import json,copy
import sys

def get_value_name_value(file_path):
    
    # 提取第一个版本的版本号
    version_name=draw_version(file_path)


    # dict_max={}
    # dict_min={}
    value_num_list=[]
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


        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))

        for i in new_line:
            if i == '':
                new_line.remove(i)

            if len(new_line)>=3:
                # print(new_line)
                # list.append(new_line[1])
                # dict_min['version']=version_name
                # dict_min['name']=new_line[1]
                # dict_tmp=copy.deepcopy(dict_min)
                # dict_max[new_line[1]]=dict_tmp
                list_tmp=[new_line[1],new_line[3]]
                value_num_list.append(list_tmp)
                break
        
        line=f.readline()
    f.close()
    return value_num_list

def draw_version(file_path):
    new_line=re.split(r'[/]',str(file_path))
    new_line=new_line[-1]
    version_name=re.sub('\D','',new_line)
    return version_name


if __name__=="__main__":
    old_value_num_list=get_value_name_value('C:/Users/Administrator/Desktop/try1/cfd_para_5389.txt')     
    # print(type(old_version_list))
    # new_version_list=get_value_name('C:/Users/Administrator/Desktop/try1/cfd_para_6425.txt')  

    print(old_value_num_list)

    # print(new_version_list)