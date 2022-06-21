#coding=UTF-8

import re
import os
import json,copy
import sys
import operator

#获取5720版本的变量名
def get_value_name(file_path):
    
    # 提取第一个版本的版本号


    # dict_max={}
    # dict_min={}
    value_num_list=[]
    f=open(file_path, 'r', encoding='UTF-8')
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

# 获取参数对比表的情况
def getSqlData(nameList):
    f = open('C:/Users/76585/Desktop/basicparam/para_compare_ver2.json', 'r')
    data = json.load(f)
    for key, value in data.items():
        print('%s:%s' % (key, value))


if __name__ == '__main__':
    # file_path='C:/Users/76585/Desktop/basicparam/cfd_para.hypara'
    # list = get_value_name(file_path)
    # print(list)