#coding=UTF-8
import pymysql

# 批量插入可以先将数据组织为二维列表，其中每一行为一条记录。比如有student表字段为：stu_id, stu_name, stu_score

# 准备数据
insert_data = [
		[1, '湍流', "visname", "visnameNew", 5720, "inner"],
		[2, '湍流', "visname", "visnameNewAgain", 9198, "inner"],
		[3, '迭代步数', "maxstep", "stepNew", 5720, "inner"]
	]

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
sql = 'INSERT INTO basic_param(id, param_name, origin_name, present_name, version, branch_name) VALUES (%s, %s, %s, %s, %s, %s)'

# 批量插入
try:
    res = cursor.executemany(sql, insert_data)
    print(res)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
finally:
    conn.close()
