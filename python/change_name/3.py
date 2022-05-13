#coding=UTF-8
#sys.setdefaultencoding("utf8")
# 找到哈希值对应的版本号，并将哈希值和版本号对应起来

import re
import os

listx=['478def', 'dfger3', 'er12', 'fbg54', 'ojvc']
dict={}

f=open('C:/Users/76585/Desktop/compare/version_haxi.txt')

#第一种循环读取文件内容
line=f.readline()
while line:
    # print line
    if 'phenglei' in line:
        # s=re.findall('"phenglei":"([\s.]+)"', line)
        # print s[-1]
        new_line=re.split(' |\n|:',str(line))
        print new_line
        for i in listx:
            if i in new_line:
                dict[i]=new_line[0]
            else:
                continue

        

        # new_list2=new_list(new_list.index('phenglei'))
        # print new_list2
        # print new_list
        # if 'phenglei' in new_list:
        #     new_line2=re
        # new_list=list(new_line)
        # print new_line

    line=f.readline()
    # print new_list

print dict

# 第二种循环读取文件内容
# for line in f.readlines():
#     print line