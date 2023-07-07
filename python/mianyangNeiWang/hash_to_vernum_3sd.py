#coding=UTF-8
# 对于每个分支的cfd_para文件，实现文件名的改变，将哈希值替换为对应的版本号
# 这个版本在2版本的基础上只替换了文件路径，版本2才是最稳定的

import os
import re

l=[]
dict={}
# f=open('C:/Users/Administrator/Desktop/version_hash_try.txt')
# f=open('C:/Users/Administrator/Desktop/one.txt')


# cfd_para.hypara存放的位置
for j in os.listdir('F:/lgf/name_split'):
# 哈希值和版本号对应的关系的文件路径
    f=open('F:/lgf/version_hash_v1.txt')

    # print j  no error

    # 获得每个文件夹里面的内容
    filelist=os.listdir('F:/lgf/name_split/'+j)
    n=0

    # print filelist  no error

    for filenames in os.listdir('F:/lgf/name_split/'+j):
        # print (filenames)
        new_line=re.split('\.',str(filenames))
        # print(new_line)
        
        # 列表l存储cfd.para文件的哈希值
        l.append(new_line[-1])



    line =f.readline()
    while line:
        # print line
        if 'PHengLEI' in line:
            new_line2=re.split('\t|\n|:|,',str(line))
            # print (new_line2)
            # print l
            for i in l:
                # if 里面的第二个判断条件，是因为以下情况
                # 版本3005提交，3006合并，两个哈希值一样。如果没有第二个判断，字典不能有相同键，后面会覆盖前面，最终是3006存在
                # 但是在生产表格，如果要回退到3005版本，因为没有3005版本存在，回去找前面的版本，但实际上3005已经更改了。
                if (i in new_line2) and (i not in dict.keys())  :
                    # 字典dict的键为哈希值，值为版本号。
                    # 因为版本号是在每一行的开头，就是列表的第一个值。所以当判断哈希值在这一行，就可以存在字典里面
                    dict[i]=new_line2[0]
                else:
                    continue

        line=f.readline()

    # print (dict)

    for i in filelist:

        oldname='F:/lgf/name_split/'+j+'/'+filelist[n]

        new_list=re.split('\.',str(filelist[n]))
        # new_list[-1]是哈希值
        if new_list[-1] in dict.keys():
            value=dict[new_list[-1]]
            # newname='C:/Users/Administrator/Desktop/cfdnames2'+'/'+'cfd_para'+'.'+value
            # 替换完成后存放的路径
            newname='F:/lgf/name_split2/'+j+'/'+'cfd_para_'+value+'.txt'
            os.rename(oldname,newname)

        n=n+1

    f.close()
    # print dict

# print (dict)


    