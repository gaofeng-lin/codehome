#coding=UTF-8

import os,re
from collections import Counter

def get_value_name(file_path):
    dict={}
    # list=[]
    f=open(file_path)
    line=f.readline()

    while line:
        tmp=line[:2]
        if tmp=='//':
            line=f.readline()
            continue
        if line.find('*')!=-1:
            line=f.readline()
            continue
        if line.find('#')!=-1:
            line=f.readline()
            continue

        new_line=re.split(r';',str(line))
        new_line1=re.split(r'=',str(new_line[0]))

        if(len(new_line1)==2):

            new_line_name=re.split(r'[\t,\s]\s*',new_line1[0])

            new_line_value_num=re.split(r'[;]',new_line1[1])

            dict[new_line_name[1]]=new_line_value_num[0].strip()
            # list.append(new_line_name[1])

        line=f.readline()
    f.close()
    return dict

def delete_same_value(old_list,new_list):
    for i in old_list:
        new_list=[0 if i==k else k for k in new_list]
    last_list=new_list
    return last_list
if __name__ == '__main__':
    # old_dict=get_value_name('C:/Users/76585/Desktop/two_dim/nochange_para_self.txt')
    # new_dict=get_value_name('C:/Users/76585/Desktop/two_dim/change_para_self.txt')

    old_dict=get_value_name('C:/Users/76585/Desktop/widy_body/nochange_para_self.txt')
    new_dict=get_value_name('C:/Users/76585/Desktop/widy_body/change_para_self.txt')
    # print list1
    # old=delete_same_value(new_l,old_l)
    # new=delete_same_value(old_l,new_l)

    # print old
    # print new

    # b=dict(Counter(new_l))
    # print ([key for key,value in b.items() if value > 1])

    # print old_dict
    # print new_dict
    for i in old_dict.keys():
        # print i
        if i in new_dict:
            # print i
            # print old_dict[i]
            # print new_dict[i]
            if old_dict[i]!=new_dict[i]:
                print i
                print 'no compute: ' + old_dict[i]
                print 'compute: ' +  new_dict[i]
                print '\n'