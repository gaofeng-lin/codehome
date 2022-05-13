#coding=UTF-8
import json


# 1.读文件

# f=open('C:/Users/76585/Desktop/param.ts','r')

# line=f.readline()

# while line:
#     print line
#     line=f.readline()

key={
"userParams" : 
  {
    'label': '昵称',
    "type": "ParamComponent.Input",
    "key": 'user_name',
    "rules": [
      { "required": "true", "message": '请输入用户昵称' },
      { "type": 'string', "whitespace": "true", "message": '用户昵称不能是空格' },
    ],
  }
}

with open("C:\\Users\\76585\\Desktop\\ts_json\\test1.json", "w+")as f:
    json.dump(key,f,sort_keys=True,indent =4,ensure_ascii=False)