#coding=UTF-8
# 实现文件名的改变，将哈希值替换为对应的版本号

import os
import re

l=[]
dict={}
f=open('C:/Users/Administrator/Desktop/version_hash_try.txt')
# f=open('C:/Users/Administrator/Desktop/one.txt')


filelist=os.listdir('C:/Users/Administrator/Desktop/name_split/Branch_Baka')
n=0



for filenames in os.listdir('C:/Users/Administrator/Desktop/name_split/Branch_Baka'):
    # print filenames
    new_line=re.split('\.',str(filenames))

    l.append(new_line[-1])




line =f.readline()
while line:
    # print line
    if 'PHengLEI' in line:
        new_line2=re.split('\t|\n|:|,',str(line))
        # print new_line2
        # print l
        for i in l:
            if i in new_line2:
                # print i
                dict[i]=new_line2[0]
            else:
                continue
    
    line=f.readline()


for i in filelist:
    
    oldname='C:/Users/Administrator/Desktop/name_split/Branch_Baka'+'/'+filelist[n]

    new_list=re.split('\.',str(filelist[n]))
    if dict.has_key(new_list[-1]):
        value=dict[new_list[-1]]
        # newname='C:/Users/Administrator/Desktop/cfdnames2'+'/'+'cfd_para'+'.'+value
        newname='C:/Users/Administrator/Desktop/name_split2/Branch_Baka'+'/'+'cfd_para_'+value+'.txt'
        os.rename(oldname,newname)

    # s=".".join(new_list[0:-1])

    # newname='C:/Users/Administrator/Desktop/cfdnames2'+'/'+'cfd_para'+'.'+value

    # os.rename(oldname,newname)
    n=n+1

# print dict


 