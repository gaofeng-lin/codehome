#coding=UTF-8
import pymysql
import json

# 打开文件
f = open(结果文件, 'r')
data = json.load(f)
res = []
tmpList = []
for key, value in data.items():
    tmpList.append(key)
    for i in range(1, len(value)):
        tmpList.append(value[i]['name'])
        tmpList.append(int(value[i]['version']))
        tmpList.append("phenglei")
        res.append(tmpList)
        tmpList = tmpList[0]
    tmpList = []
# 连接数据库
conn = pymysql.connect(host=host,
                       user=user, password=pwd,
                       database=database, charset='utf8')
cursor = conn.cursor()
# sql语句
sql = 'INSERT INTO basic_param(origin_name, present_name, version, branch_name) VALUES (%s, %s, %s, %s)'
# 批量插入
try:
    res = cursor.executemany(sql, res)
    print(res)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    conn.close()
