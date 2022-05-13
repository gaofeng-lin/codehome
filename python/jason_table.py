#coding=UTF-8

#json格式存储数据,核心思想是在字典里面放字典,二级字典的值是多个字段组成的列表。
# 总共需要两层字典。

import json
import os,re
import copy
import jsonpath

# key={ "value1": [
# { "v": 200 ,"name":"value1"},
# { "v": 300, "name":"value2"},
# ]
# ,
# "value3":[
#    { "v": 400,"needcheck":"true"} 
# ],
# "value2": [
# { "v": 200 ,"name":"value1"},
# { "v": 300, "name":"value2"},
# {  "v": 300, "name":"value3","needcheck":"true" }
# ]
# }

def try1():

    key={ "value1": [
    { "v": 200 ,"name":"value1"},
    { "v": 300 ,"name":"value2"}
    ]
    ,
    "value3":[
    { "v": 200,"name":"value3"} 
    ],
    "value2": [
    { "v": 200 ,"name":"value2"}
    ]
    }

    for i in key:
        if isinstance(key[i],dict):
            print i

# key = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ,{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }]



# print(json.dumps(key,sort_keys=True,indent =4,ensure_ascii=False))

# with open("C:\\Users\\76585\\Desktop\\try2\\test.json", "w+")as f:
#     json.dump(key,f,sort_keys=True,indent =4,ensure_ascii=False)


# 1.生成初始表格
def init_table(init_path):
    dict=get_bianliang(init_path)
    # print dict
    with open("C:\\Users\\76585\\Desktop\\try2\\test.json", "w+")as f:
        json.dump(dict,f,sort_keys=True,indent =4,ensure_ascii=False)

# 2.向已有json文件追加内容
def add_value_firclass():
    new_data={"value2": {"v": 200 ,"name":"value2"}}
    with open("C:\\Users\\76585\\Desktop\\try2\\test.json", "r") as f:
        old_data=json.load(f)
        old_data.update(new_data)
    with open("C:\\Users\\76585\\Desktop\\try2\\test.json", "w") as f:
        json.dump(old_data, f)

# 3.向已有json文件追加二级内容
def add_value_secclass():
    new_data={'v': 400 ,"name":"a2"}
    f=open("C:\\Users\\76585\\Desktop\\try2\\test.json", "r")
    
    old_data=json.load(f)
    f.close()
       
        # print old_data['a']


        # if 'a' in old_data:
        #     print 'yes'
        # else:
        #     print 'no'

        # print type(old_data['a'])

        # dict={'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}
        # if 'on' in dict.values()=='True':
        #     print 'yes'
        # else:
        #     print 'no'

    for i in old_data:
        if isinstance(old_data[i],list):
            for j in old_data[i]:
                if 'a1' in j.values():
                    old_data[i].append(new_data)
                    f=open("C:\\Users\\76585\\Desktop\\try2\\test.json", "w")
                    json.dump(old_data,f,sort_keys=True,indent =4,ensure_ascii=False)
                    break
        else:
            continue


        # for i in old_data['a']:
        #     print i
        #     # for values in i.values():
        #     #     print values

        #     if 'a1' in i.values():
        #         print 'a1 存在'
        #         break
        #     else:
        #         # print 'a1 不存在'
        #         continue
            # for j in i:
            #     print j
                # print old_data['a'][j]

            # print j
       
        


    #     if isinstance(old_data['a1'],dict):
    #         dict_tmp=[old_data['a']]

    #     dict_tmp.append(new_data)
        
    #     old_data['a']=dict_tmp
       
    # with open("C:\\Users\\76585\\Desktop\\try2\\test.json", "w") as f:
    #     json.dump(old_data, f)

# 通过传入文件的路径，获取文件的变量名并存储在列表里面，最后返回一个列表
def get_bianliang(file_path):
    
    dict_mid={}
    dict_min={}
    # list=[]
    f=open(file_path)
    line=f.readline()
    while line:

        tmp=line[:2]
        if tmp == '//':
            line=f.readline()
            continue
                
        if line.find('#')!=-1:
            line=f.readline()
            continue

        new_line=re.split(r'[;,\t,\s,=,\n]\s*',str(line))
        
        for i in new_line:
            if i=='':
                new_line.remove(i)
                
            if len(new_line)>=3:
              
                dict_min['v']=200
             
                dict_min['name']=new_line[1]
                dict_tmp=copy.deepcopy(dict_min)      
               
                dict_mid[new_line[1]]=dict_tmp

            
                break
                
            
        line=f.readline()

    f.close()
    return dict_mid

if __name__ == '__main__':

    # init_table('C:/Users/76585/Desktop/cfdname1/cfd_para_304.txt')
    # add_value_firclass()
    add_value_secclass()
    # try1()
