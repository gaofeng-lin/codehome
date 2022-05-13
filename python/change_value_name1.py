#coding=UTF-8
import os
import re
import json
import shutil
#1.读param.ts文件,将变量存储到列表中
# init_path=os.getcwd().replace('\\','/')
# init_path=os.getcwd()
# cfd_para_self_path='/home/yskj/lgf/case_new/Sphere_default/Default/bin/cfd_para_self.hypara'
# param_cmp_path=init_path+'/para_compare_ver2.json'
def get_param_value(cfd_para_self_path):
    f=open(cfd_para_self_path, 'r')

    line=f.readline()
    list_param=[]
    count=1    
    count_list=[]

    while line:
        tmp=line[:2]
        if tmp=='//':
            line=f.readline()
            count=count+1
            continue
        if line.find('*')!=-1:
            line=f.readline()
            count=count+1
            continue
        if line.find('#')!=-1:
            line=f.readline()
            count=count+1
            continue
        
        new_line=re.split(r';',str(line))
        new_line1=re.split(r'=',str(new_line[0]))

        if len(new_line1)==2:
            new_line_name=re.split(r'[\t,\s]\s*',new_line1[0])
            list_param.append(new_line_name[1])
            count_list.append(count)
        line=f.readline()
        count=count+1
    f.close()
    return [list_param,count_list]

    # while line:
    #     # print line
    #     if 'key' in line:
    #         # print line
    #         line_tmp=re.split(r'[:,\n,\t]',line)
    #         tmp_key=line_tmp[0].strip()
    #         if tmp_key=='key':
    #             if "'" in line_tmp[1]:
    #                 list_param.append(eval(line_tmp[1]))
    #                 count_list.append(count)
    #     line=f.readline()
    #     count=count+1
    # f.close()
    # return [list_param,count_list]

# 2.读取para_compare_ver2.json文件，将变量名存入列表

def get_change_value(param_cmp_path,list_param,index_list):
    list_value_change=[]
    new_version=9198
    f=open(param_cmp_path,'r')
    data=json.load(f)
    f.close()
    index_l=[]

    for key in data:
        # print len(data[key])
        if len(data[key])<=2:
            for i in list_param:
                if i ==data[key][0]['name']:
                    if new_version>=int(data[key][1]['version']):
                        # print i+' --- '+data[key][1]['name']
                        list_tmp=[i,data[key][1]['name']]
                        list_value_change.append(list_tmp)
                        index_l.append(index_list[list_param.index(i)])
                        break
                    else:
                        # print i+' not change'
                        break
                if i==data[key][1]['name']:
                    # print i +' not change'
                    break
        else:
            for i in list_param:
                if i ==data[key][0]['name']:
                    if new_version>=int(data[key][1]['version']) and new_version<int(data[key][2]['version']) :
                        # print i+' --- '+data[key][1]['name']
                        list_tmp=[i,data[key][1]['name']]
                        list_value_change.append(list_tmp)
                        index_l.append(index_list[list_param.index(i)])
                        break
                    if new_version>=int(data[key][2]['version']) :
                        # print i+' --- '+data[key][2]['name']
                        list_tmp=[i,data[key][2]['name']]
                        list_value_change.append(list_tmp)
                        index_l.append(index_list[list_param.index(i)])
                        break
                    else:
                        # print i+' not change'
                        break
                if i==data[key][1]['name']:
                    if new_version>=int(data[key][2]['version']) :
                        # print i+' --- '+data[key][2]['name']
                        list_tmp=[i,data[key][2]['name']]
                        list_value_change.append(list_tmp)
                        index_l.append(index_list[list_param.index(i)])
                        break

                if i==data[key][2]['name']:
                    # print i+' not change'
                    break
    return [list_value_change,index_l]
# 3.修改param.ts文件

def overwrite_param_file(tmp_para_path,list_value_change,index_l):
    f=open(tmp_para_path,'r')
    line=f.readline()
    tmp_list=[]

    while line:
        tmp_list.append(line)
        line=f.readline()
    f.close()
    f=open(tmp_para_path,'w')
    count=1
    for line in tmp_list:
        if count in index_l:
            tmp_index=index_l.index(count)
            # line='    key: '+"'"+list_value_change[tmp_index][1]+"'"+','
            if list_value_change[tmp_index][0]=='gridUnit':
                line='double '+list_value_change[tmp_index][1]+'      =  1;'
                f.write('%s\n' %line)
                count=count+1
            else:
                line=line.replace(list_value_change[tmp_index][0],list_value_change[tmp_index][1])
                f.write('%s' %line)
                count=count+1
        else:
            f.write('%s' %line)
            count=count+1
    f.close()
       

if __name__=='__main__':
    init_path=os.getcwd()
    for filename in os.listdir('/home/yskj/phserver/static/case/'):
        if filename!='Rae2822_default':
            cfd_para_self_path='/home/yskj/phserver/static/case/'+filename+'/Default/bin/cfd_para_self.hypara'
            param_cmp_path=init_path+'/para_compare_ver2.json'
            list_end=get_param_value(cfd_para_self_path)
            # print list_end[1]
            list_param=list_end[0]
            index_list=list_end[1]
            get_change_value_res=get_change_value(param_cmp_path,list_param,index_list)
            list_value_change=get_change_value_res[0]
            index_l=get_change_value_res[1]
            # index_l表示要修改位置的行数，list_value_change表示要修改表里的对应关系[old_name,new_name]
            # print index_l
            # print list_value_change
            # print index_l
            overwrite_param_file(cfd_para_self_path,list_value_change,index_l)

            # 复制新版cfd_para文件
            shutil.copy('/home/yskj/lgf/PHengLEI-9198/PHengLEI/examples/bin/cfd_para.hypara','/home/yskj/phserver/static/case/'+filename+'/Default/bin/')

    