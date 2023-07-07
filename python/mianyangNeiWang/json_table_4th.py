#coding=UTF-8
# 在版本3的基础上，将生成的json文件放到对应的目录下面

# 最终生成的文件名是分支名.json。因为每一个分支下提交了不同版本的cfd_para，程序会根据路径把分支名提取出来。这里是把3个
# cfd_para放到了try1文件夹，所以最终生成的文件是try1.json

import re
import os
import json,copy
import sys



init_path='C:/Users/Administrator/Desktop/try1'
file_name_list=re.split(r'[/]',str(init_path))
file_name=file_name_list[-1]

def init_table(init_path):
    

    file_list=sort_version_list(init_path)
    if file_list==[]:
        return
    path=init_path+'/'+file_list[0]

    # 提取第一个版本的版本号
    # version_name=draw_version(path)

    dict=get_value_name(path)

    # print(dict)

    with open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w') as f:
        json.dump(dict,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.close()

    f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','w')
    f.close()
    

def init_manual_check_file(version_num,val_list):

    dict_max={}
    dict_min={}
    val_list=list(set(val_list))
    val_list.remove(0)
    for i in val_list:
        dict_min['version']=version_num
        dict_min['name']=i
        dict_min['check']='false'
        dict_min['state']=' '
        dict_min['old_name']=' '
        dict_tmp=copy.deepcopy(dict_min)
        dict_max[i]=dict_tmp
    
    return dict_max

def manual_check(new_version_num,list):

    if os.path.getsize('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json')==0:
        dict=init_manual_check_file(new_version_num,list)
        with open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','w') as f:
            json.dump(dict,f,sort_keys=True,indent=4,ensure_ascii=False)
            f.close()

    else:
        for j in list:
            if j==0:
                continue
            new_data={j:{'name':j,'version':new_version_num,'check':'false','state':' ','old_name':' '}}
            f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','r')

            old_data=json.load(f)

            old_data.update(new_data)  

            f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','w')

            json.dump(old_data,f,indent=4,ensure_ascii=False)
            f.flush()

            f.close()

def add_done_field(value):
    f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','r')
    old_data=json.load(f)

    old_data[value]['done']=' '

    f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','w')
    json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.flush()
    f.close()

def from_manual_check_to_paracmp():
    
    # 1.判断这个变量是否已经放到了版本对比表格里面，如果没有放到里面了，不用管，继续运行
    # 如果没有放到里面，执行相关操作，完成以后追加一个字段 "done"，后面必须加一个值 "done":"" 都行，不然会报错

    # 读取文件
    f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','r')
    old_data=json.load(f)
    f.close()


    # key是变量名
    for key in old_data:
        # print(old_data[key])
        if 'done' not in old_data[key].keys():
           
            # print(old_data[key]['name'])
            if old_data[key]['state'] == 'new value':
                print('add new value')
                add_value_firclass(old_data[key]['version'],key)

                add_done_field(key)


            if old_data[key]['state'] == 'change name':
                print('change name')
                add_value_secclass(old_data[key]['old_name'],key,old_data[key]['version'])

                add_done_field(key)

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

    # 下面这个是判断新增是只有一个变量，还是变量列表（变量数量大于等于2会存在列表里面）
    if isinstance(new_value,list):
        for i in new_value:
            new_data={i:{'name':i,'version':new_version_num}}
            f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','r')
            old_data=json.load(f)

   
    
            old_data.update(new_data)  

            f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w')



            json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
            f.flush()

            f.close()
    else:

        new_data={new_value:{'name':new_value,'version':new_version_num}}
        f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','r')

        old_data=json.load(f)
        old_data.update(new_data)  

        f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w')

        json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
        f.flush()

        f.close()




def add_value_secclass(old_value,new_value,new_version_num):
    f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','r')
    new_data={'name':new_value,'vesion':new_version_num}

    old_data=json.load(f)

    f.close()

    # 如果二级变量存放的是列表，那么里面的变量是无法直接查到的，会进入else里面
    if old_value in old_data:
        dict_tmp=[old_data[old_value]]

        dict_tmp.append(new_data)
        old_data[old_value]=dict_tmp

        f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w')
        json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
        f.flush()
        f.close()

    else:
        for i in old_data:
            if isinstance(old_data[i],list):
                for j in old_data[i]:
                    if new_value in j.values():
                        new_data1={'name':new_value,'vesion':new_version_num}
                        old_data[i].append(new_data1)
                        f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w')
                        json.dump(old_data,f,sort_keys=True,indent=4,ensure_ascii=False)
                        f.flush()
                        f.close()

            else:
                continue



# 这个函数的目的是为了将两个列表的长度用0补为相同，0在末尾追加
# def complete_len(old_list,new_list):
#     if(len(old_list)>=len(new_list)):
#         l1=len(old_list)-len(new_list)
#         while(l1!=0):
#             new_list.append(0)
#             l1=l1-1
        
#     else:
#         l1=len(new_list)-len(old_list)
#         while(l1!=0):
#             old_list.append(0)
#             l1=l1-1
#     l_end=[old_list,new_list]
#     return l_end

def add_value_to_file(new_version_num,old_version_unique,new_version_unique):
    
    # f=open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w')
    # old_version_unique.append(0)
    # new_version_unique.append(0)

    # l_end=complete_len(old_version_unique,new_version_unique)
    # old_version_unique=l_end[0]
    # new_version_unique=l_end[1]

    # 在列表头尾部添加一个0，不改变 变量相对位置，确保列表不越界
    old_version_unique.insert(0,0)
    new_version_unique.insert(0,0)
    old_version_unique.append(0)
    new_version_unique.append(0)


    for i in new_version_unique:
        if i==0:
            continue
        index_new=new_version_unique.index(i)

        # 如果新版本的索引超过了老版本变量的长度，直接manual_check
        if index_new>=(len(old_version_unique)-1):
            print ('need manual_check, list index out of range')
            # sys.exit()
            # 用list_tmp存储i，将变量类型转换为列表，因为manual_check函数的输入是将多个变量存放列表读取
            # 如果只传单变量，会读取单个字符。 另一个办法就是在manual_check里面加一个判断条件
            list_tmp=[i]
            manual_check(new_version_num,list_tmp)
            continue
        # 新版变量和旧版本变量都不为0，两个版本变量索引的前一个位置和后一个位置均为0.认为新版变量是旧版本变量的改名
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


        # 新版变量不为0，旧版在（该索引处，前一个位置，后一个位置索引）均为0.认为新版变量是新增的
        # 上述判断方法仍然存在缺陷，相同变量如果新版本与老版相差一定的行数（比如5行），可能会判断错误，正确的或许是改名

        if old_version_unique[index_new] ==0 and old_version_unique[index_new+1]==0 and old_version_unique[index_new-1]==0:
            len_diff=len(old_version_unique)-len(new_version_unique)
            if(len_diff>=0):
                # len_diff=len(old_version_unique)-len(new_version_unique)
                if old_version_unique[index_new+len_diff] ==0 and old_version_unique[index_new+1+len_diff]==0 and old_version_unique[index_new-1+len_diff]==0:
                    add_value_firclass(new_version_num,i)
                    new_version_unique[index_new]=0  
                    continue
            else:
                if old_version_unique[index_new+len_diff] ==0 and old_version_unique[index_new+1+len_diff]==0 and old_version_unique[index_new-1+len_diff]==0:
                    add_value_firclass(new_version_num,i)
                    new_version_unique[index_new]=0  
                    continue

        
        #下面是原来，可以正确运行的 
        # if old_version_unique[index_new] ==0 and old_version_unique[index_new+1]==0 and old_version_unique[index_new-1]==0:
            
        #     add_value_firclass(new_version_num,i)
        #     new_version_unique[index_new]=0  
        #     continue

        
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

        # 判断manual_check文件中是否存在 false字符，存在则程序停止;如果不存在则执行函数from_manual_check_to_paracmp
        flag=check_file('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json')
        if flag == 'manual_check':
            print ('need manual cheak,input ok when you finish')

            con=input("input:")
            
            if con=='ok':
                from_manual_check_to_paracmp()

            # os.system('pause')
            # from_manual_check_to_paracmp()
        
            # os.system('pause')
            # from_manual_check_to_paracmp()

        # if flag == 'have done':
        #     continue

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

            # 同名变量置0后，如果新版本全为0，直接比较比较下一个版本
            if len(set(new_version_unique))==1:
                continue
            # if len(old_version_unique)!=0 and len(new_version_unique)!=0:
            # 列表里面的存储的变量都没有变为0，这时候出现了改名的情况，需要人工校验
            if len(set(old_version_unique))!=1 and len(set(new_version_unique))!=1:
                manual_check_list=add_value_to_file(new_version_num,old_version_unique,new_version_unique)
              
                if len(set(manual_check_list))==1:
                    continue
                else: 
                    manual_check(new_version_num,manual_check_list)


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


def check_file(manual_json_file_path):
    f=open(manual_json_file_path,'r')
    if os.path.getsize(manual_json_file_path) ==0:
        return 'null'
    # list=f.readlines()
    # print (list)
    line=f.readline()
    while line:
        if 'false' in line:
            return 'manual_check'
        line=f.readline()
    
    return 'have done'

if __name__ == '__main__':

    init_table('C:/Users/Administrator/Desktop/try1')

    comapre_folder('C:/Users/Administrator/Desktop/try1')

    # flag=check_file('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json')
    # if flag == 'manual_check':
    #     print ('end')