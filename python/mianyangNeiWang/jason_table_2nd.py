#coding=UTF-8
# json生成表格

import re
import os
import json,copy
import sys

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


    dict_max={}
    dict_min={}
    f=open(file_path)
    line=f.readline()

    while line:
        tmp=line[:2]
        if tmp == '//' :
            line=f.readline()
            continue


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


def add_value_firclass(new_version_num,new_value):

    if isinstance(new_value,list):
        for i in new_value:
            new_data={i:{'name':i,'version':new_version_num}}
            f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','r')
            old_data=json.load(f)

   
    
            old_data.update(new_data)  

            f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')



            json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
            f.flush()

            f.close()
    else:

        new_data={new_value:{'name':new_value,'version':new_version_num}}
        f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','r')

        old_data=json.load(f)
        old_data.update(new_data)  

        f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')

        json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
        f.flush()

        f.close()




def add_value_secclass(old_value,new_value,new_version_num):
    f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','r')
    new_data={'name':new_value,'vesion':new_version_num}

    old_data=json.load(f)

    f.close()
    if isinstance(old_data[old_value],dict):
        dict_tmp=[old_data[old_value]]

    dict_tmp.append(new_data)
    old_data[old_value]=dict_tmp
  

    f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')

   
    
    json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.flush()

    f.close()


def manual_check(new_version_num,list):
    # for i in list:
    #     if i==0:
    #         list.remove(i)
    
    for j in list:
        if j==0:
            continue
        new_data={j:{'name':j,'version':new_version_num,'needcheck':'true'}}
        f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','r')

        old_data=json.load(f)

        # f.close()

        old_data.update(new_data)  

        f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')



        json.dump(old_data,f,indent=4,ensure_ascii=False)
        f.flush()

        f.close()



def add_value_to_file(new_version_num,old_version_unique,new_version_unique):
    
    # f=open('C:/Users/Administrator/Desktop/cfd_version/all_version.json','w')
    old_version_unique.append(0)
    new_version_unique.append(0)

    for i in new_version_unique:
        if i==0:
            continue
        index_new=new_version_unique.index(i)
        # 新版变量不为0，旧版在该索引，前，后索引均为0.认为新版变量是新增的
        if old_version_unique[index_new] ==0 and old_version_unique[index_new+1]==0 and old_version_unique[index_new-1]==0:
            add_value_firclass(new_version_num,i)
            new_version_unique[index_new]=0
            continue
        for j in old_version_unique:
            if j==0:
                continue
            # index_new=new_version_unique.index(i)
            index_old=old_version_unique.index(j)
            if index_old==index_new :
                if old_version_unique[index_old-1]==0 and old_version_unique[index_old+1]==0 and new_version_unique[index_new+1]==0 and new_version_unique[index_new-1]==0:
                    add_value_secclass(j,i,new_version_num)
                    # old_version_unique[index_old]=0
                    new_version_unique[index_new]=0
                    break
   

    return new_version_unique
        
def delete_same_value(old_list,new_list):
    for i in old_list:
        new_list=[0 if i==k else k for k in new_list]
    
    last_list=new_list
    return last_list


# 迭代比较整个文件夹里面的文件
def comapre_folder(file_path):
    file_one=os.listdir(file_path)
    if len(file_one)==1:
        return
    
    file_list=sort_version_list(file_path)

    for i in range(len(file_list)):

        # 判断文件是否含有needcheck字符，如果有，里面停止
        flag=check_file('C:/Users/Administrator/Desktop/cfd_version/all_version.json')
        if flag == 'manual_check':
            print ('need manual cheak')
            sys.exit()

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
                manual_check_list=add_value_to_file(new_version_num,old_version_unique,new_version_unique)
              
                manual_check(new_version_num,manual_check_list)
                # print ('end l')
                # f.close()

            else:
                new_version_only_have=[i for i in new_version_list if i not in old_version_list]
                add_value_firclass(new_version_num,new_version_only_have)

                

# 单独比较两个文件，并修改json文件
def compare_double_file(oldfile_path,newfile_path):
    old_version_list=get_value_name(oldfile_path)
    new_version_list=get_value_name(newfile_path)
    common_have=[i for i in new_version_list if i in old_version_list]
    
    old_version_unique=delete_same_value(new_version_list,old_version_list)
    new_version_unique=delete_same_value(old_version_list,new_version_list)
    
    new_line=re.split(r'[/]',str(newfile_path))
    new_line=new_line[-1]
    new_version_num=re.sub('\D','',new_line)
    # if len(old_version_unique)!=0 and len(new_version_unique)!=0:
    # 列表里面的存储的变量都没有变为0，这时候出现了改名的情况，需要人工校验
    if len(set(old_version_unique))!=1 and len(set(new_version_unique))!=1:
        manual_check_list=add_value_to_file(new_version_num,old_version_unique,new_version_unique)
      

        manual_check(new_version_num,manual_check_list)
        # print ('end l')
        # f.close(
    else:
        new_version_only_have=[i for i in new_version_list if i not in old_version_list]
        add_value_firclass(new_version_num,new_version_only_have)


def check_file(json_file_path):
    f=open(json_file_path,'r')
    # list=f.readlines()
    # print (list)
    line=f.readline()
    while line:
        if 'needcheck' in line:
            return 'manual_check'
            break

        line=f.readline()

if __name__ == '__main__':

    init_table('C:/Users/Administrator/Desktop/try1')

    comapre_folder('C:/Users/Administrator/Desktop/try1')

    # flag=check_file('C:/Users/Administrator/Desktop/cfd_version/all_version.json')
    # if flag == 'manual_check':
    #     print ('end')