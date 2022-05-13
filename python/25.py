#coding=UTF-8

# 生成特殊的列表

import re

l1=['a1','a2','a3','a4','string','cfdVER','Poel','a5','a6','udp','a7','a8','stng','cfdVR','Pol','a9','a10','a11','a12','a13','strings','cfdVsER','Podel','WE','a14','a15','a16','a17','a18','a19','a20']

# l2=['a1','a2','a3','a4','string','cfdVER','Poel','a5','a6','udp','a7','a8','stng','cfdVR','Pol','a9','a10','a11','a12','a13','strings','cfdVsER','Podel','WE','a14','a15','a16','a17','a18','a19','a20']
l2=['a1','a2','a3','a4','string','cfdVER','Poel','a5','a6','udp','a7','a8','a9','a10','a11','a12','a13','strings','cfdVsER','Podel','WE','a14','a15','a16','a17','a18','a19','a20']


def draw_start_end_len(list):
    l2=[]
    i=0
    while i<len(list):
        list_tmp=re.split(r'\d+',list[i])
        if list_tmp[0]!='a':
            count1=i-1
            num1=list[count1]
            for j in range(i,len(list)):
                list_tmp=re.split(r'\d+',list[j])
                if list_tmp[0]=='a':
                    count2=j
                    num2=list[count2]
                    l3=[num1,num2,count2-count1-1]
                    l2.append(l3)
                    i=j
                    break
        else:
            i=i+1
    return l2

def sure_state(new_list,new_uniqu_list,old_list):
    i=0
    for list_tmp in new_uniqu_list:
        num1=list_tmp[0]
        num2=list_tmp[1]
        len=list_tmp[2]

        if old_list.index(num2)-old_list.index(num1)-1==0:
            print "new value"
            index1=new_list.index(num1)
            index2=new_list.index(num2)

            for j in range(index1+1,index2):
                # 下面输出的变量是需要改名的变量
                print new_list[j]

        if old_list.index(num2)-old_list.index(num1)-1==len:
            # 对于改名字，还要再建立一个字典，key是变量名，value是变量值；或者用列表存值，因为索引是不变的
            # 这一步需要得到这个范围内变量的索引，然后再比较它们的值是否全部相同，如果全部相同就认为改名，有一个不同就不行
            index_new=range(new_list.index(num1),new_list.index(num2)+1)
            index_old=range(old_list.index(num1),old_list.index(num2)+1)

            new_tmp=[]
            old_tmp=[]
            for i in index_new:
                # 括号里面 new_list.index(i),这个列表需要将新版本的值存进来
                new_tmp.append()
            for i in index_old:
                # 括号里面 old_list.index(i)，这个列表需要将旧版本的值存进来
                old_tmp.append()
            
            #然后判断两个列表是否完全相同，可以用operator方法，在tmp.py文件里面 

            print "change name"


if __name__=='__main__':
    l3=draw_start_end_len(l1)
    print l3
    # sure_state(l1,l3,l2)

    # list_t=range(0,9)
    # print list_t


