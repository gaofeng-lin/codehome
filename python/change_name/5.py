#coding=UTF-8
# 修订后的版本，可以直接拿来使用

import os
import re

l=[]
dict={}
f=open('C:/Users/76585/Desktop/compare/version_haxi.txt')
filelist=os.listdir('C:/Users/76585/Desktop/cfdname')
n=0

# 获取目录文件名，并进行切割
for filenames in os.listdir('C:/Users/76585/Desktop/cfdname'):
    new_line1=re.split('\.',str(filenames))
    l.append(new_line1[-1])

# 找到哈希值对应的版本号，并将哈希值和版本号对应起来,存入字典
line=f.readline()
while line:
    # print line
    if 'phenglei' in line:
        new_line2=re.split(' |\n|:',str(line))
        for i in l:
            if i in new_line2:
                dict[i]=new_line2[0]
            else:
                continue
    line=f.readline()

# 根据哈希值和版本号，修改文件名字
for i in filelist:
    oldname='C:/Users/76585/Desktop/cfdname'+'/'+filelist[n]

    # print oldname
    new_list=re.split('\.',str(filelist[n]))
    value= dict[new_list[-1]]

    # filelist[n]=".".join(new_list)

    # 名字切割
    # new_list=re.split('\.',str(filelist[n]))
    s=".".join(new_list[0:-1])

    newname='C:/Users/76585/Desktop/cfdname'+'/'+s+'.'+value

    # print newname

    os.rename(oldname,newname)
    n=n+1
