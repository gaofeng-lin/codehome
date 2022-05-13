#coding=UTF-8

# 对文件夹下的文件按文件名的编号进行排序，存入列表。在迭代读取列表，更新表格。

import os,re

from queue import Queue
# import queue


file_path='C:/Users/76585/Desktop/cfdname1'
file_list=os.listdir(file_path)

# for file in file_list:
#     # position='C:/Users/76585/Desktop/shell/cfdname2'+'/'+file
#     # print position
#     # print file
#     new_line=re.sub('\D','',str(file))
#     print new_lin

# 按照某个关键字进行排序
file_list.sort(key=lambda x:int(x[9:-4]))


# q=Queue(maxsize=0)

# q.put(file_list)

# print type(file_list)

# for x,y in file_list:
#     print x
#     print y

for i in range(0,len(file_list),1):
    l1=file_list[i:i+2]
    if len(l1)==2:
        print file_path+l1[0]
        print file_path+l1[1]


# for file in file_list:
#     q.put(file)
#     # print file

# while not q.empty():
#     print q.get()


# print q.queue