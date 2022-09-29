#coding=UTF-8
import pymysql
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

print(res)

# 批量插入可以先将数据组织为二维列表，其中每一行为一条记录。比如有student表字段为：stu_id, stu_name, stu_score

# 准备数据
# insert_data = [
# 		["visname", "visnameNew", 5720, "inner"],
# 		["visname", "visnameNewAgain", 9198, "inner"],
# 		["maxstep", "stepNew", 5720, "inner"]
# 	]

# 连接数据库
host = '121.37.93.92'  # 地址
user = 'root'  # 用户名
pwd = 'SBcaiyong@PASSword123'  # 密码
database = 'phenglei'  # 数据库名

conn = pymysql.connect(host=host,
                       user=user, password=pwd,
                       database=database, charset='utf8')
cursor = conn.cursor()

# sql语句
sql = 'INSERT INTO basic_param(origin_name, present_name, version, branch_name) VALUES (%s, %s, %s, %s)'

# 批量插入
# try:
#     res = cursor.executemany(sql, res)
#     print(res)
#     conn.commit()
# except Exception as e:
#     print(e)
#     conn.rollback()
# finally:
#     conn.close()
