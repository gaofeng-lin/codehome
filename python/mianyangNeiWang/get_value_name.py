#coding=UTF-8

import re
import os
import json,copy
import sys
import operator

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

def get_value_name(file_path):
    
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
          
                # list_tmp=[new_line[1],new_line[3]]
                value_num_list.append(new_line[1])
                break
        
        line=f.readline()
    f.close()
    return value_num_list

def draw_version(file_path):
    new_line=re.split(r'[/]',str(file_path))
    new_line=new_line[-1]
    version_name=re.sub('\D','',new_line)
    return version_name

def delete_same_value(old_list,new_list):
    for i in old_list:
        new_list=[0 if i==k else k for k in new_list]
    
    last_list=new_list
    return last_list

def zero_to_serise(list1):
    j=1
    for i in list1:
        if i==0:
            list1[list1.index(i)]='a'+str(j)
            j=j+1
    return list1



def delete_zero(list1):
    for i in list1[::-1]:
        if i==0:
            list1.remove(i)
    return list1

def draw_start_end_len(list):
    l2=[]
    i=0
    while i<len(list):
        list_tmp=re.split(r'\d+',list[i])
        if list_tmp[0]!='a':
            count1=i-1
            num1=list[count1]
            for j in range(i,len(list)):
                list_tmp=re.split(r'\d+',list[j])
                if list_tmp[0]=='a':
                    count2=j
                    num2=list[count2]
                    l3=[num1,num2,count2-count1-1]
                    l2.append(l3)
                    i=j
                    break
        else:
            i=i+1
    return l2

def check_value_num(old_list,new_list):
    if operator.eq(old_list,new_list)==True:
        return 'yes'
    else:
        return 'no'

def sure_state(new_list,new_uniqu_list,old_list):
    i=0
    for list_tmp in new_uniqu_list:
        num1=list_tmp[0]
        num2=list_tmp[1]
        index_len=list_tmp[2]

        if old_list.index(num2)-old_list.index(num1)-1==0:
            print('new value')

            new_value_list=new_list[new_list.index(num1)+1:new_list.index(num2)]
            print(new_value_list)

        if old_list.index(num2)-old_list.index(num1)-1==index_len:

            print('change name')

            # 输出需要改名字的变量：old_value,new_value,new_version_num
            new_value_name_list=new_list[new_list.index(num1)+1:new_list.index(num2)]
            old_value_name_list=old_list[old_list.index(num1)+1:old_list.index(num2)]

            old_dict_tmp=get_value_name_and_value('C:/Users/Administrator/Desktop/try1/cfd_para_5389.txt')
            new_dict_tmp=get_value_name_and_value('C:/Users/Administrator/Desktop/try1/cfd_para_6425.txt')

            new_follow_list=[]
            old_follow_list=[]

            for i in new_value_name_list:
                new_follow_list.append(new_dict_tmp[i])
            for i in old_value_name_list:
                old_follow_list.append(old_dict_tmp[i])


            # # print(new_value_name_list)
            # # print(old_value_name_list)
            print(old_follow_list)
            print(new_follow_list)
            flag=check_value_num(new_follow_list,old_follow_list)
            # if flag=='yes':
            #     print('可以改名')
            print(flag)
    

if __name__=="__main__":


    # old_dict=get_value_name_and_value('C:/Users/Administrator/Desktop/try1/cfd_para_5389.txt')
    # print(old_dict)

    old_version_list=get_value_name('C:/Users/Administrator/Desktop/try1/cfd_para_5389.txt')     
    new_version_list=get_value_name('C:/Users/Administrator/Desktop/try1/cfd_para_6425.txt')   


    # old_version_list=[]
    # new_version_list=[]

    # for i in old_list:
    #     old_version_list.append(i[0])
    # for j in new_list:
    #     new_version_list.append(j[0])


    old_version_unique=delete_same_value(new_version_list,old_version_list)
    new_version_unique=delete_same_value(old_version_list,new_version_list)

    # print(len(old_version_unique))
    # print(new_version_unique)
 
    old_version_unique=zero_to_serise(old_version_unique)
    new_version_unique=zero_to_serise(new_version_unique)

    # 下面这个列表，是多个列表组成的，每个列表有三个元素组成。举例：[[a1,a2,4],[a4,a5,2]] 表示a1,a2之间有4个变量在旧版本里面没有
    new_unique_list=draw_start_end_len(new_version_unique)
    # print(new_unique_list)

    sure_state(new_version_unique,new_unique_list,old_version_unique)

