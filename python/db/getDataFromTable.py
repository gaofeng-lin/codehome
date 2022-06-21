#coding=UTF-8

import json

f = open('C:/Users/76585/Desktop/basicparam/para_compare_ver3.json', 'r')

data = json.load(f)

res = []
tmpList = []

for key, value in data.items():
    # print('%s:%s' % (key, value))
    # print(len(value))
    tmpList.append(key)
    for i in range(1, len(value)):
        # print(value[i]['name'])
        # print(value[i]['vesion'])
        tmpList.append(value[i]['name'])
        tmpList.append(int(value[i]['version']))
        tmpList.append("phenglei")
        res.append(tmpList)
        tmpList = tmpList[0]
    tmpList = []

print (res)

