#coding=UTF-8
import pymysql
import json

# 将参数变更情况按照memcached接受的格式导出到文件

f = open('C:/Users/76585/Desktop/basicparam/para_compare_ver3.json', 'r')

data = json.load(f)

res = []
tmpList = []



# key是私有云的变量名
for key, value in data.items():
    # print('%s:%s' % (key, value))
    # print(len(value))
    tmpList.append(key)
    for i in range(1, len(value)):
        # print(value[i]['name'])
        # print(value[i]['vesion'])
        tmpList.append(value[i]['name'])
        # tmpList.append(int(value[i]['version']))
        # tmpList.append("phenglei")

        with open('C:/Users/76585/Desktop/memcached.txt', "a") as f:
            restring = "add " + key + " 0 0 " + str(len((value[i]['name']).encode())) 
            f.write(restring)
            f.write("\n")
            f.write(value[i]['name'])
            f.write("\n")

            restring = "add " + value[i]['name'] + " 0 0 " + str(len(key.encode())) 
            f.write(restring)
            f.write("\n")
            f.write(key)
            f.write("\n")
        res.append(tmpList)
        tmpList = tmpList[0]
    tmpList = []

# print(res)

