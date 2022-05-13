#coding=UTF-8

# 根据哈希值和版本号，修改文件名字
import os
import re

dist={'478def': '9', 'fbg54': '14', 'er12': '12', 'dfger3': '10', 'ojvc': '16'}


filelist=os.listdir('C:/Users/76585/Desktop/cfdname')

n=0 
for i in filelist:
    oldname='C:/Users/76585/Desktop/cfdname'+'/'+filelist[n]

    # print oldname
    new_list=re.split('\.',str(filelist[n]))
    value= dist[new_list[-1]]

    # filelist[n]=".".join(new_list)

    # 名字切割
    # new_list=re.split('\.',str(filelist[n]))
    s=".".join(new_list[0:-1])

    newname='C:/Users/76585/Desktop/cfdname'+'/'+s+'.'+value

    # print newname

    os.rename(oldname,newname)
    n=n+1