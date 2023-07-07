#coding=UTF-8
# 在版本3的基础上，将生成的json文件放到对应的目录下面

# 最终生成的文件名是分支名.json。因为每一个分支下提交了不同版本的cfd_para，程序会根据路径把分支名提取出来。这里是把3个
# cfd_para放到了try1文件夹，所以最终生成的文件是try1.json

import re
import os
import json,copy
import sys
import operator


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

    dict=get_value_name_value_dict(path)

    # print(dict)

    with open('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json','w') as f:
        json.dump(dict,f,sort_keys=True,indent=4,ensure_ascii=False)
    f.close()

    f=open('C:/Users/Administrator/Desktop/cfd_version/'+'manual_check'+'.json','w')
    f.close()
    

def init_manual_check_file(version_num,val_list):

    dict_max={}
    dict_min={}
    if 0 in val_list:
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
                # print('add new value')
                add_value_firclass(old_data[key]['version'],key)

                add_done_field(key)


            if old_data[key]['state'] == 'change name':
                # print('change name')
                add_value_secclass(old_data[key]['old_name'],key,old_data[key]['version'])

                add_done_field(key)

def get_value_name_and_value(file_path):
    
    # 提取第一个版本的版本号
    version_name=draw_version(file_path)
    dict={}
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

        # new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
        new_line=re.split(r';',str(line))
        new_line1=re.split(r'=',str(new_line[0]))
        # print(new_line1)
        if len(new_line1)==2:
         

            new_line_name=re.split(r'[\t,\s]\s*',new_line1[0])
            # print(new_line_name[1])

            new_line_value_num=re.split(r'[;]',new_line1[1])
            # print(new_line_value_num[0].strip())

            # 存储的是变量名和变量值
            dict[new_line_name[1]]=new_line_value_num[0].strip()
            # list1.append(new_line_name[1])
          
        line=f.readline()
    f.close()
    return dict


def get_value_name_value_dict(file_path):
    
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
                # list_end.append(new_line[1])
                break
        
        line=f.readline()
    f.close()
    return dict_max

def get_value_name(file_path):
    
    # 提取第一个版本的版本号
    version_name=draw_version(file_path)


    dict_max={}
    dict_min={}
    list_end=[]
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
                # dict_min['version']=version_name
                # dict_min['name']=new_line[1]
                # dict_tmp=copy.deepcopy(dict_min)
                # dict_max[new_line[1]]=dict_tmp
                list_end.append(new_line[1])
                break
        
        line=f.readline()
    f.close()
    return list_end


def zero_to_serise(list1):
    j=1
    for i in list1:
        if i==0:
            list1[list1.index(i)]='a'+str(j)
            j=j+1
    return list1



def delete_zero(list1):
    for i in list1[::-1]:
        if i==0:
            list1.remove(i)
    return list1

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

def check_value_num(old_list,new_list):
    if operator.eq(old_list,new_list)==True:
        return 'yes'
    else:
        return 'no'

def sure_state(new_list,new_uniqu_list,old_list,new_version_num,old_dict_tmp,new_dict_tmp,new_value_check):
    # new_list,old_list是把0变为a1,a2。new_uniqu_list是[[a1,a2,3],[a5,a6,12]]这种形式
    i=0
    for list_tmp in new_uniqu_list:
        num1=list_tmp[0]
        num2=list_tmp[1]
        index_len=list_tmp[2]

        if old_list.index(num2)-old_list.index(num1)-1==0:
            print('new value')

            new_value_list=new_list[new_list.index(num1)+1:new_list.index(num2)]
            # print(new_value_list)
            # for i in new_value_list:
            #     add_value_firclass(new_version_num,i)
            # new_list[new_list.index(num1)+1:new_list.index(num2)]=0

            for i in range(new_list.index(num1)+1,new_list.index(num2)):
                add_value_firclass(new_version_num,new_list[i])
                new_value_check[i]=0



        if old_list.index(num2)-old_list.index(num1)-1==index_len:

            print('change name')

            # 输出需要改名字的变量：old_value,new_value,new_version_num
            new_value_name_list=new_list[new_list.index(num1)+1:new_list.index(num2)]
            old_value_name_list=old_list[old_list.index(num1)+1:old_list.index(num2)]

            # old_dict_tmp=get_value_name_and_value('C:/Users/Administrator/Desktop/try1/cfd_para_5389.txt')
            # new_dict_tmp=get_value_name_and_value('C:/Users/Administrator/Desktop/try1/cfd_para_6425.txt')

            new_follow_list=[]
            old_follow_list=[]

            for i in new_value_name_list:
                new_follow_list.append(new_dict_tmp[i])
            for w in old_value_name_list:
                old_follow_list.append(old_dict_tmp[w])

        
            flag=check_value_num(new_follow_list,old_follow_list)
            if flag=='yes':
                # 下面的逻辑有点问题。new_follow_list,old_follow_list里面存放的是被认为改名变量的变量值
                # 走到这一步。new_follow_list,old_follow_list里面的值是一一对应的
                k=0
                while k<len(old_value_name_list):
                    new_value=new_value_name_list[k]
                    old_value=old_value_name_list[k]
                    # 里面放的应该是变量名
                    add_value_secclass(old_value,new_value,new_version_num)
                    # 把new_list的某处的变量清0
                    new_value_check[new_list.index(new_value)]=0
                    k=k+1
            # print(flag)
    return new_value_check
    


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
            # 得到的是嵌套字典，key是变量名，值是变量名和版本号组成的字典
            old_version_list=get_value_name(file_path+'/'+l1[0])
            new_version_list=get_value_name(file_path+'/'+l1[1])



            # 这是字典，key是变量名，值是变量值
            old_value_name_dict=get_value_name_and_value(file_path+'/'+l1[0])
            new_value_name_dict=get_value_name_and_value(file_path+'/'+l1[1])

            # common_have=[i for i in new_version_list if i in old_version_list]


            # 相同变量置0，后面变为a1,a2,a3
            old_version_unique=delete_same_value(new_version_list,old_version_list)
            new_version_unique=delete_same_value(old_version_list,new_version_list)

            # 相同变量置0,后面不会变为a1,a2,a3
            old_have_zero=copy.deepcopy(old_version_unique) 
            new_have_zero=copy.deepcopy(new_version_unique)

            
            new_line=re.split(r'[/]',str(file_path+'/'+l1[1]))
            new_line=new_line[-1]

            new_version_num=re.sub('\D','',new_line)

            # 同名变量置0后，如果新版本全为0，直接比较比较下一个版本
            if len(set(new_have_zero))==1:
                continue

            # if len(old_version_unique)!=0 and len(new_version_unique)!=0:
            # 列表里面的存储的变量都没有变为0，这时候可能出现了改名的情况，需要人工校验
            if len(set(new_have_zero))!=1 and len(set(old_have_zero))!=1:
                
                # 这一步把0转换为数列。a1,a2,a3
                old_version_unique1=zero_to_serise(old_version_unique)
                new_version_unique1=zero_to_serise(new_version_unique)

                # new_uniqu_list是[[a1,a2,3],[a5,a6,12]]这种形式
                new_unique_list=draw_start_end_len(new_version_unique)

                manual_check_list=sure_state(new_version_unique1,new_unique_list,old_version_unique1,new_version_num,old_value_name_dict,new_value_name_dict,new_have_zero)

                 #下面的是最开始的，上面的是改动的
                # manual_check_list=add_value_to_file(new_version_num,old_version_unique,new_version_unique)
              
                if len(set(manual_check_list))==1:
                    continue
                else: 
                    manual_check(new_version_num,manual_check_list)


            else:
                new_version_only_have=[i for i in new_version_list if i not in old_version_list]
                if len(new_version_only_have)!=0:
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

    # init_table('C:/Users/Administrator/Desktop/try1')

    comapre_folder('C:/Users/Administrator/Desktop/try1')

    # flag=check_file('C:/Users/Administrator/Desktop/cfd_version/'+file_name+'.json')
    # if flag == 'manual_check':
    #     print ('end')