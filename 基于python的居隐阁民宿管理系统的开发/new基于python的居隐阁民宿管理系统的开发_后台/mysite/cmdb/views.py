from django.shortcuts import render
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import json

sys.path.append("./")
from django.shortcuts import HttpResponse
# Create your views here.
import pymysql
from DBUtils.PooledDB import PooledDB
import uuid
import time
import datetime

mysqlInfo = {
    # "host": 'localhost',
    "host": 'localhost',
    # 'host':'192.168.1.51',
    "user": 'root',
    "passwd": '123',
    # "db": 'hospital',
    "db": 'bs_kezhan',
    "port": 3306,
    "charset": 'utf8',

}


class OPMysql(object):
    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.coon = OPMysql.getmysqlconn()
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=5, maxcached=10, host=mysqlInfo['host'],
                              user=mysqlInfo['user'], passwd=mysqlInfo['passwd'], db=mysqlInfo['db'],
                              port=mysqlInfo['port'], charset=mysqlInfo['charset'])
            # print(__pool)
        return __pool.connection()

    # 插入\更新\删除sql
    def op_insert(self, sql):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num  # 写入单条数据返回1
        except Exception as e:
            self.coon.rollback()
            print(e)
            return 2

    # 写入数据一条
    def op_list(self, sql, lcrist):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql, lcrist)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num  # 写入单条数据返回1
        except Exception as e:
            self.coon.rollback()
            print(e)
            return 2

    # 写入数据二条
    def op_list_two(self, sql, lcrist, sql2, lcrist2):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql, lcrist)
            insert_num = self.cur.execute(sql2, lcrist2)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num
        except:
            self.coon.rollback()
            return 2

    # 写入数据三条
    def op_list_three(self, sql, lcrist, sql2, lcrist2, sql3, lcrist3):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql, lcrist)
            insert_num = self.cur.execute(sql2, lcrist2)
            insert_num = self.cur.execute(sql3, lcrist3)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num
        except Exception as e:
            self.coon.rollback()
            print(e)
            return 2
        # 写入数据四条

    def op_list_four(self, sql, lcrist, sql2, lcrist2, sql3, lcrist3, sql4, lcrist4):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql, lcrist)
            insert_num = self.cur.execute(sql2, lcrist2)
            insert_num = self.cur.execute(sql3, lcrist3)
            insert_num = self.cur.execute(sql4, lcrist4)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num
        except Exception as e:
            self.coon.rollback()
            print(e)
            return 2

    # 写入数据五条
    def op_list_five(self, sql, lcrist, sql2, lcrist2, sql3, lcrist3, sql4, lcrist4, sql5, lcrist5):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql, lcrist)
            insert_num = self.cur.execute(sql2, lcrist2)
            insert_num = self.cur.execute(sql3, lcrist3)
            insert_num = self.cur.execute(sql4, lcrist4)
            insert_num = self.cur.execute(sql5, lcrist5)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num
        except Exception as e:
            self.coon.rollback()
            print(e)
            return 2

    # 写入数据6条
    def op_list_six(self, sql, lcrist, sql2, lcrist2, sql3, lcrist3, sql4, lcrist4, sql5, lcrist5, sql6, lcrist6):
        try:
            # print('查询语句', sql)
            insert_num = self.cur.execute(sql, lcrist)
            insert_num = self.cur.execute(sql2, lcrist2)
            insert_num = self.cur.execute(sql3, lcrist3)
            insert_num = self.cur.execute(sql4, lcrist4)
            insert_num = self.cur.execute(sql5, lcrist5)
            insert_num = self.cur.execute(sql6, lcrist6)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num
        except Exception as e:
            self.coon.rollback()
            print(e)
            return 2

    # 查询
    def op_select(self, sql):
        try:
            # print('查询语句', sql)
            self.cur.execute(sql)  # 执行sql
            select_res = self.cur.fetchone()  # 返回结果为字典
            # print('查询结果', select_res)
            return select_res
        except:
            return 2

    def op_select_new(self, sql, data):
        try:
            # print('查询语句', sql)
            self.cur.execute(sql, data)  # 执行sql
            select_res = self.cur.fetchone()  # 返回结果为字典
            # print('查询结果', select_res)
            return select_res
        except Exception as e:
            print(e)
            return 2

    def op_select_one(self, sql):
        try:
            # print('查询语句', sql)
            self.cur.execute(sql)  # 执行sql
            sqlon_data = self.cur.fetchall()  # 返回结果为列表
            # print('查询结果', sqlon_data)
            return sqlon_data
        except Exception as e:
            print(e)
            return 2

    def sqlon(self, sql, data):
        try:
            # print('查询语句', sql)
            self.cur.execute(sql, data)  # 执行sql
            sqlon_data = self.cur.fetchall()  # 返回结果为列表
            # print('查询结果', sqlon_data)
            return sqlon_data
        except Exception as e:
            print(e)
            return 2

    def sql_many(self, sql, data):
        try:
            # print('写入语句', sql)
            insert_num = self.cur.executemany(sql, data)
            # print('查询结果 sucess ', insert_num)
            self.coon.commit()
            return insert_num  # 写入单条数据返回1
        except:
            self.coon.rollback()
            return

    # 释放资源
    def dispose(self):
        self.coon.close()
        self.cur.close()


def state(state, msg):
    response = HttpResponse(json.dumps({"code": state, "msg": msg}))
    response["Access - Control - Allow - Origin"] = "*"
    response["Access - Control - Allow - Methods"] = "POST, GET, OPTIONS"
    response["Access - Control - Max - Age"] = "1000"
    response["Access - Control - Allow - Headers"] = "*"
    return response


def now_time():
    # now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 将python的datetime转换为unix时间戳
    dtime = datetime.datetime.now()
    un_time = int(time.mktime(dtime.timetuple()))
    times = datetime.datetime.fromtimestamp(un_time)
    return str(times)


def form(data):
    form = {"code": 1, "msg": "查询成功", "data": data, "time": now_time(), "key": ""}
    form["num"] = len(form["data"])
    response = HttpResponse(json.dumps(form))
    response["Access - Control - Allow - Origin"] = "*"
    response["Access - Control - Allow - Methods"] = "POST, GET"
    response["Access - Control - Max - Age"] = "1000"
    response["Access - Control - Allow - Headers"] = "*"
    return response


def add_user(request):
    a = json.loads(request.body)
    sql = "insert into user(name, password, id, type,z_name,telephone) values (%s,%s,%s,%s,%s,%s)"
    sql_val = [a["user_name"], a["user_password"], str(uuid.uuid1()), 1, a["z_name"], a["telephone"]]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "注册成功")
    else:
        return state(2, "注册失败")


def login_user(request):
    a = json.loads(request.body)
    sql = "select name,id,z_name,telephone from user where name=%s and password=%s and type=1"
    sql_val = [a["user_name"], a["user_password"]]
    opm = OPMysql()
    resdata = opm.op_select_new(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:
        return state(2, "登录失败")


def select_all_user(request):
    sql = "select * from user where type=1"
    opm = OPMysql()
    resdata = opm.op_select_one(sql)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:
        return state(2, "失败")


def del_user(request):
    a = json.loads(request.body)
    sql = "update user set type=2 where id=%s"
    sql_val = [a["id"]]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "删除成功")
    else:
        return state(2, "删除失败")


def add_home(request):
    a = json.loads(request.body)
    sql = "insert into home(money, nenber, body, ya_money, type, path, state,id) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_val = [a["money"], a["nenber"], a["body"], a["ya_money"], 1, a["path"], 2, str(uuid.uuid1())]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")


def del_home(request):
    a = json.loads(request.body)
    sql = "update home set type=2 where id=%s"
    sql_val = [a["id"]]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")


def select_all_home(request):
    sql = "select * from home where type=1 and state=2"
    opm = OPMysql()
    resdata = opm.op_select_one(sql)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:
        return state(2, "失败")


def xiandan(request):
    a = json.loads(request.body)
    sql = "INSERT INTO `bs_kezhan`.`order`(`user_id`, `home_id`, `id`, `ya_money`, `money`, `type`, `time`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    sql_val = [a["user_id"], a["home_id"], str(uuid.uuid1()), a["ya_money"], a["money"], "1", now_time()]
    sql_two="update home set state=1 where id=%s"
    sql_two_val=[a["home_id"]]
    opm = OPMysql()
    resdata = opm.op_list_two(sql, sql_val,sql_two,sql_two_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")


def check_in_data(request):
    sql = "SELECT `order`.ya_money,`order`.money,`order`.id,`user`.z_name,`user`.telephone,home.body,home.nenber,home.path,order.time as in_time FROM `order` INNER JOIN `user` ON `order`.user_id=`user`.id INNER JOIN home ON `order`.home_id=home.id WHERE `order`.type=1"
    opm = OPMysql()
    resdata = opm.op_select_one(sql)
    opm.dispose()
    if resdata != 2:
        for row in resdata:
            row["in_time"]=str(row["in_time"])
        return form(resdata)
    else:

        return state(2, "失败")


def check_in(request):
    a = json.loads(request.body)
    sql="update `order` set type=2 where id=%s"
    sql_val=[a["id"]]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")

def select_in_dianpu(request):
    sql = "SELECT `order`.ya_money,`order`.money,`order`.id,`user`.z_name,`user`.telephone,home.body,home.nenber,home.path FROM `order` \
    INNER JOIN `user` ON `order`.user_id=`user`.id INNER JOIN home ON `order`.home_id=home.id WHERE `order`.type=2"
    opm = OPMysql()
    resdata = opm.op_select_one(sql)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:
        return state(2, "失败")


def select_out_dianpu(request):
    sql = "SELECT `order`.ya_money,`order`.money,`order`.id,`user`.z_name,`user`.telephone,home.body,home.nenber,home.path,`order`.plun FROM `order` \
    INNER JOIN `user` ON `order`.user_id=`user`.id INNER JOIN home ON `order`.home_id=home.id WHERE `order`.type=3"
    opm = OPMysql()
    resdata = opm.op_select_one(sql)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:
        return state(2, "失败")


def check_out(request):
    a = json.loads(request.body)
    sql = "update `order` set type=3 where id=%s"
    sql_val = [a["id"]]
    sql_two="update home set state=2 where id=(select home_id from `order` where `order`.id=%s)"
    sql_two_val=[a["id"]]
    opm = OPMysql()
    resdata = opm.op_list_two(sql, sql_val,sql_two,sql_two_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")


def select_all_user_order(request):
    a = json.loads(request.body)
    sql = "SELECT `order`.ya_money,`order`.money,`order`.id,`user`.z_name,`user`.telephone,home.body,home.nenber,home.path,`order`.type,`order`.plun FROM `order` \
    INNER JOIN `user` ON `order`.user_id=`user`.id INNER JOIN home ON `order`.home_id=home.id WHERE `user`.id=%s"
    sql_val=[a["id"]]
    opm = OPMysql()
    resdata = opm.sqlon(sql,sql_val)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:
        return state(2, "失败")


def insert_gonggao(request):
    a = json.loads(request.body)
    sql="insert into `gonggao`(msg, title, id) VALUES (%s,%s,%s)"
    sql_val=[a["msg"],a["title"],str(uuid.uuid1())]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")

def select_gonggao(request):
    sql="select * from gonggao"
    opm = OPMysql()
    resdata = opm.op_select_one(sql)
    opm.dispose()
    if resdata != 2:
        return form(resdata)
    else:

        return state(2, "失败")

def into_plun(request):
    a = json.loads(request.body)
    sql="update `order` set plun=%s where id=%s"
    sql_val=[a["plun"],a["id"]]
    opm = OPMysql()
    resdata = opm.op_list(sql, sql_val)
    opm.dispose()
    if resdata != 2:
        return state(1, "成功")
    else:
        return state(2, "失败")