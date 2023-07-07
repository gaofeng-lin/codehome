#coding=UTF-8
# 将ActiveBranch里面的cfd_para文件提取出版本号，通过git log cfd_para将得到的哈希值转为版本号，再将两个进行比较。


import os
import re,sys

# l1用来存放ActiveBranch里面的cfd_para文件的版本号,
# l2用来存放git log cfd_para哈希值转为版本号后的版本号
l1=[]
l2=[]
dict={}

# 1.提取ActiveBranch里面的cfd_para文件的版本号存入列表
filelist=os.listdir('C:/Users/Administrator/Desktop/name_split2/ActiveBranch')

for file in filelist:
    ver_num=re.findall(r'\d+',str(file))
    # print(type(ver_num))
    l1.append(ver_num[0])
    # print(ver_num)

print(l1)

#2.通过git log cfd_para将得到的带哈希值的cfd_para文件存到name_split3这个文件夹里面。这个只能在phenglei,phengleios里面运行


#3.将文件里面的哈希值存入列表,再转换为版本号
f=open('C:\\Users\\Administrator\\Desktop\\name_split3\\hash.txt')

line=f.readline()

while line:
    line=re.split('\n',str(line))
    l2.append(line[0])    
    line=f.readline()
f.close()

# print(l2)
# l2[l2.index('c210599e0dff38428beed63e81afd0580d372b9b')]=10
# print(l2)


f1=open('C:/Users/Administrator/Desktop/version_hash_try.txt')

line=f1.readline()
while line:
    
    if 'PHengLEI' in line:
         new_line2=re.split('\t|\n|:|,',str(line))
         # print (new_line2)
         # print l
         for i in l2:
             if (i in new_line2)  :
                l2[l2.index(i)]=new_line2[0]
             else:
                 continue


    line=f1.readline()
f1.close()

print(l2)

# 3.两个列表进行对比，
l3=[x for x in l1 if x not in l2]

if l3==l1:
    print('no change')
else:
    print('change')