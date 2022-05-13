#coding=UTF-8

import json
import os,re
import copy

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

# print(json.dumps(key,sort_keys=True,indent =4,ensure_ascii=False))
# print type(key['value1'])

list1=[{'name': 'value1', 'v': 200}, {'name': 'value2', 'v': 300}]

key['value2']=list1
print(json.dumps(key,sort_keys=True,indent =4,ensure_ascii=False))
