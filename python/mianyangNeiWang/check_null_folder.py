#coding=UTF-8

#判断空文件夹

import os

path='C:/Users/Administrator/Desktop/name_split'
foleders=os.listdir(path)

for foleder in foleders:
    foleder2=os.listdir(path+'/'+foleder)
    # print foleder2
    if foleder2==[]:
        os.rmdir(path+'/'+foleder)

# print foleders