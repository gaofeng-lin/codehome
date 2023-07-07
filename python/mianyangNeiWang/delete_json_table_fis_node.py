#coding=UTF-8

# 读取try1.json文件，将里面一层的节点删除，只保留有存储变量修改的节点

import re
import os
import json,copy
import sys
import operator

result_path='F:/lgf/'
file_name='para_ver_cmp'
f=open(result_path+file_name+'.json','r')


old_data=json.load(f)
f.close()

new_date=old_data

# 这个列表用来存储需要删除的变量
list_tmp=[]

for i in new_date:
    if isinstance(new_date[i],dict):
        # print('dict')
        list_tmp.append(i)



for i in list_tmp:
    del new_date[i]

print('\n')

# print(len(new_date))
    # print(type(new_date[i]))

with open('C:/Users/Administrator/Desktop/cfd_version/'+'para_ver_cmp_simplify_v3'+'.json','w') as f:
    json.dump(new_date,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.close()

# print(type(old_data))