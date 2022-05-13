#coding=UTF-8

# 获取文件里面的变量名
import re,os
# dict={}


def get_bianliang(file_path):
    # dict={}
    list=[]
    f=open(file_path)
    line=f.readline()
    # print type(line)
    while line:
                # new_line=re.split(r'(;, ,\t,=,\n)\s',str(line))
        if line.find('#')!=-1:
            line=f.readline()
            continue
        if line.find('//')!=-1:
            line=f.readline()
            continue
        
        print line
        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
                # new_line=re.split('\W|\n\s',str(line))
                # new_line.remove("''")
                # new_list=list(new_line)
        # print new_line
                # 去掉列表里面的 ''
        for i in new_line:
            if i=='':
                new_line.remove(i)
                
            if len(new_line)==3:
                # print new_line
                # dict[new_line[1]]=[new_line[0],new_line[2]]
            #    dict[new_line[1]]=[new_line[2]]
                list.append(new_line[1])
                
                
        line=f.readline()
    return list



if __name__ == '__main__':
    # dict1={}
    # dict2={}
    # list1=[]
    # list2=[]
    list1=get_bianliang('C:/Users/76585/Desktop/cfdname1/cfd_para_355.txt')
    list2=get_bianliang('C:/Users/76585/Desktop/cfdname1/cfd_para_383.txt')

    print list1
    print list2

    # a = [x for x in list1 if x in list2]

    # for x in list1 if x in list2:

    #     list1.remove(x)
    # print list2
