#coding=UTF-8
import pymysql
import json

# 这个代码是为了将参数变化以mptt的形式存入数据库


# 连接数据库
host = '121.37.93.92'  # 地址
user = 'root'  # 用户名
pwd = 'SBcaiyong@PASSword123'  # 密码
database = 'phenglei'  # 数据库名

conn = pymysql.connect(host=host,
                       user=user, password=pwd,
                       database=database, charset='utf8')
cursor = conn.cursor()


def get_list_from_file():
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
    return res

def get_value(sql):
    a=1
    try:
    # res = cursor.executemany(sql,3)
        cursor.execute(sql)
        a = cursor.fetchall()[0][0]
        print(cursor.fetchall()[0][0])
    # print(a)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()
    return a

def db_sql(sql):

    try:
    # res = cursor.executemany(sql,3)
        cursor.execute(sql)
        # a = cursor.fetchall()[0][0]
        # print(cursor.fetchall()[0][0])
    # print(a)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


# 构造一个节点
def create_node(p_name, n_level):

    get_target_id = 'select @target_id:=MAX(node_id) from mptt where node_level=%s' % (n_level)
    target_id = get_value(get_target_id)

    get_nrgt = 'rgt from mptt where node_id = %s' % (target_id)
    nrgt = get_value(get_nrgt)

    update_rgt = 'update mptt set rgt = rgt + 2 where rgt >= %s' %(nrgt)
    update_lft = 'update mptt set lft = lft + 2 where lft >= %s' %(nrgt)

    db_sql(update_rgt)
    db_sql(update_lft)

    insert_sql = 'insert into mptt (node_name, lft, rgt, node_level) values(%s, %s, %s + 1, %s)' % (p_name, nrgt, nrgt, n_level)
    db_sql(insert_sql)

    # return res

# 插入完整的结构
def inset_whole_data(res):

    # print(res)
    for i in res:
        create_node()
        print(i[3])



if __name__ == '__main__':

    # sql = 'select @target_id:=MAX(node_id) from mptt where node_level=4'
    # res = create_node("test",4)
    # print(res)

    res = get_list_from_file()
    inset_whole_data(res)


