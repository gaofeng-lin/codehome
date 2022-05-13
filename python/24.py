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


data=json.loads(json.dumps(key))

for i in data:
    # print data[i]
    if isinstance(data[i],list):
        print data[i]

# print data