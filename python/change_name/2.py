#coding=UTF-8

# 获取目录文件名，并进行切割
import os 
import re
l=[]

for filenames in os.listdir('C:/Users/76585/Desktop/cfdname'):

    # l.append(filenames)
    print filenames
    new_line=re.split('\.',str(filenames))
    # print new_line
    # new_list=list(new_line)

    l.append(new_line[-1])
    # print new_list


print l