#coding=UTF-8
# json生成表格

import re
import os
import json,copy

def init_table(init_path):
    

    file_list=sort_version_list(init_path)
    if file_list==[]:
        return
    path=init_path+'/'+file_list[0]

    # 提取第一个版本的版本号
    # version_name=draw_version(path)

    dict=get_value_name(path)

    with open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w') as f:
        json.dump(dict,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.close()
    

def get_value_name(file_path):
    
    # 提取第一个版本的版本号
    version_name=draw_version(file_path)

    # list=[]
    dict_max={}
    dict_min={}
    f=open(file_path)
    line=f.readline()
    # tmp=line.decode('utf-8')
    # tmp=line[:2]
    while line:
        tmp=line[:2]
        if tmp == '//' :
            line=f.readline()
            continue
        # if line.find('//')!=-1:
        #      if tmp == '//' :
        #         line=f.readline()
        #         continue

        if line.find('*')!=-1:
            line=f.readline()
            continue

        if line.find('#')!=-1:
            line=f.readline()
            continue


        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))

        for i in new_line:
            if i == '':
                new_line.remove(i)

            if len(new_line)>=3:
                # list.append(new_line[1])
                dict_min['version']=version_name
                dict_min['name']=new_line[1]
                dict_tmp=copy.deepcopy(dict_min)
                dict_max[new_line[1]]=dict_tmp
                break
        
        line=f.readline()
    f.close()
    return dict_max

def draw_version(file_path):
    new_line=re.split(r'[/]',str(file_path))
    new_line=new_line[-1]
    version_name=re.sub('\D','',new_line)
    return version_name


def sort_version_list(file_path):

    file_list=os.listdir(file_path)
    file_list.sort(key=lambda x:int(x[9:-4]))
    return file_list


def add_value_secclass(old_value,new_value,new_version_num):
    f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','r')
    new_data={'name':new_value,'vesion':new_version_num}

    old_data=json.load(f)

    f.close()
    if isinstance(old_data[old_value],dict):
        dict_tmp=[old_data[old_value]]

    dict_tmp.append(new_data)
    old_data[old_value]=dict_tmp
    # print (old_data[old_value])

    f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')

    # json.dump(old_data,f)
   
    
    json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.flush()
    f.close()


def manual_check(new_version_num,old_version_unique,new_version_unique):
    
    # f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')

    for i in new_version_unique:
        if i==0:
            continue
        if old_version_unique[new_version_unique.index(i)]!=0:
            add_value_secclass(old_version_unique[new_version_unique.index(i)],i,new_version_num)
    # add_value_secclass('nStatisticalStep','startStatisticStep',921)
    # for i in old_version_unique:
    #     if i==0:
    #         continue
    #     for j in new_version_unique:
    #         index_old=old_version_unique.index(i)
    #         index_new=new_version_unique.index(j)
    #         if j==0:
    #             continue
    #         elif index_old==index_new :
    #             add_value_secclass(i,j,new_version_num)
    #             break
    #         else:
    #             pass
            # index_old=old_version_unique.index(i)
            # index_new=new_version_unique.index(j)
            # 值不为0表示在新版本没找到这个变量，要确定是改名，要值不为0，索引相同，且前后两个索引均为0
            # if i!=0 and j!=0 and index_old==index_new :
            #     # if old_version_unique(index_old-1)==0 and old_version_unique(index_old+1)==0 and new_version_unique(index_new+1)==0 and new_version_unique(index_new-1)==0:
            #     add_value_secclass(i,j,new_version_num)
                    
            #     break

def delete_same_value(old_list,new_list):
    for i in old_list:
        new_list=[0 if i==k else k for k in new_list]
    
    last_list=new_list
    return last_list

def compare(file_path):
    file_one=os.listdir(file_path)
    if len(file_one)==1:
        return
    
    file_list=sort_version_list(file_path)

    for i in range(len(file_list)):
        l1=file_list[i:i+2]
        if len(l1)==2:

            old_version_list=get_value_name(file_path+'/'+l1[0])
            new_version_list=get_value_name(file_path+'/'+l1[1])

            common_have=[i for i in new_version_list if i in old_version_list]


            
            old_version_unique=delete_same_value(new_version_list,old_version_list)
            new_version_unique=delete_same_value(old_version_list,new_version_list)

            new_line=re.split(r'[/]',str(file_path+'/'+l1[1]))
            new_line=new_line[-1]

            new_version_num=re.sub('\D','',new_line)

            # if len(old_version_unique)!=0 and len(new_version_unique)!=0:
            # 列表里面的存储的变量都没有变为0，这时候出现了改名的情况，需要人工校验
            if len(set(old_version_unique))!=1 and len(set(new_version_unique))!=1:
                manual_check(new_version_num,old_version_unique,new_version_unique)
                print ('end l')

            else:
                c=[i for i in new_version_list if i not in old_version_list]

                




if __name__ == '__main__':
    # list=[]
    # list=get_value_name('C:/Users/Administrator/Desktop/cfdnames2/cfd_para_304.txt')

    # print list
    # init_table('C:/Users/Administrator/Desktop/name_split2/Branch_Baka')

    # compare('C:/Users/Administrator/Desktop/name_split2/Branch_Baka')

    init_table('C:/Users/Administrator/Desktop/try1')
    compare('C:/Users/Administrator/Desktop/try1')