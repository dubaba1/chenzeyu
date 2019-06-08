import time
import datetime
import pymysql
from DBUtils.PooledDB import PooledDB
import uuid
import json
import redis
import urllib.request
import urllib.parse
import requests
import ssl
import math
# import OpenSSL #安装语句 sudo python3 -m pip install Scrapy   sudo python3 -m pip install pyopenssl
import sys
import sys, os
from flask import jsonify
mysqlInfo = {
    # "host": 'localhost',
     "host":'localhost',
    # 'host':'192.168.1.51',
    "user": 'root',
    "passwd": 'root',
    # "db": 'hospital',
    "db": 'bs_kezhan',
    "port": 3306,
    "charset": 'utf8',

}

#######################################################
# 功能描述：时间类处理工具
#######################################################
# 功能2018-11-10 21:27:10转时间戳
def to_timeStamp(otherStyleTime):
    timeArray = time.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    timeStamp_new = int(time.mktime(timeArray))
    return timeStamp_new


# 功能1541856430.9228518转格式化时间
def to_otherStyletime(timeStamp):
    '''
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime
    '''
    return datetime.datetime.fromtimestamp(timeStamp)


def xx_otherStyletime(timeStamp):
    '''
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime
    '''
    return datetime.datetime.fromtimestamp(timeStamp)


# 返回时间区间   单位日！！！！！
'''
参数说明
start_time：开始时间   时间戳来的
end_time：结束时间
'''


def to_zones(start_time, end_time):
    '''
    start_date=xx_otherStyletime(start_time)
    end_date=xx_otherStyletime(end_time)
    start_sec = time.mktime(time.strptime(start_date,'%Y-%m-%d'))
    end_sec = time.mktime(time.strptime(end_date,'%Y-%m-%d'))
    work_days = int((end_sec - start_sec)/(24*60*60))
    return work_days
    '''
    start_time = to_otherStyletime(start_time).strftime('%Y-%m-%d %H:%M:%S')
    end_time = to_otherStyletime(end_time).strftime('%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    d1 = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    # 间隔天数
    day = (d2 - d1).days
    # 间隔秒数
    # second = (d2 - d1).seconds
    f_data = zhuantime((d2 - d1).seconds)
    return {"day": day, "hours": f_data}


# 返回当前时间戳
def new_time():
    return unix_time()


# 返回格式化后时间
def now_time():
    # now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 将python的datetime转换为unix时间戳
    dtime = datetime.datetime.now()
    un_time = int(time.mktime(dtime.timetuple()))
    times = datetime.datetime.fromtimestamp(un_time)
    return str(times)


def unix_time():
    dtime = datetime.datetime.now()
    un_time = int(time.mktime(dtime.timetuple()))
    return un_time


# 时间转化秒数转格式化后的时分秒
def zhuantime(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


#######################################################
# 功能描述：数据库连接池工具
#######################################################
'''
    opm = OPMysql()
    res = opm.sqlon(sql)
    #释放资源
    opm.dispose()
'''


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
            __pool = PooledDB(creator=pymysql, mincached=10, maxcached=30, host=mysqlInfo['host'],
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


# 非法字符串检测
def sql_filter(sql, max_length=20):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")", "%", "@", "!"]
    for stuff in dirty_stuff:
        sql = sql.replace(stuff, "")
    return sql[:max_length]

#######################################################
# 功能描述：状态返回模块
#######################################################
def state(state, msg):
    error_data={"code":state,"msg":msg}
    # return json.dumps(error_data,ensure_ascii=False, indent=4)
    return jsonify(error_data)


#######################################################
# 功能描述：停车场http——post请求
#######################################################
def post_http(url, data):
    data = urllib.parse.urlencode(data)  # data是请求的form表单内容，字典格式
    data = data.encode('utf-8')
    request = urllib.request.Request(url)
    # adding charset parameter to the Content-Type header.
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")  # 请求头参数
    # request.addheaders = [('User-agent', 'Mozilla/5.0')]
    f = urllib.request.urlopen(request, data)
    # print(f.read().decode('utf-8'))
    return f.read().decode('utf-8')


def get_http(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    r = requests.get(url, verify=False)
    return r.json()


def get_out_ip():
    url = r'http://www.trackip.net/'
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find('title') + 6:txt.find('/title') - 1]
    return ip


# 字典键值排序使用工具
'''
>> sorted(dict2list(dic), key=lambda x:x[0], reverse=True) # 按照第0个元素降序排列
[('c', 1), ('b', 2), ('a', 3)]
>> sorted(dict2list(dic), key=lambda x:x[0], reverse=False) # 按照第0个元素升序排列
[('a', 3), ('b', 2), ('c', 1)]
>> sorted(dict2list(dic), key=lambda x:x[1], reverse=True) # 按照第1个元素降序排列
[('a', 3), ('b', 2), ('c', 1)]
>> sorted(dict2list(dic), key=lambda x:x[1], reverse=False) # 按照第1个元素降序排列
[('c', 1), ('b', 2), ('a', 3)]
'''


def dict2list(dic: dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst


'''
生成订单号
'''


def order_num():
    return str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))


# json构建
def json_data(data):
    # return json.dumps({"state":1,"data":data,"msg":"查询成功"},ensure_ascii=False, indent=4,sort_keys=False)
    return jsonify({"state": 1, "data": data, "msg": "查询成功"})


def layui_form(data):
    layui = {"state": 1, "msg": "查询成功"}
    layui.update(data)
    layui["count"] = len(data["data"])
    # return json.dumps(layui,ensure_ascii=False, indent=4,sort_keys=False)
    return jsonify(layui)

def form(data):
    form = {"code": 1, "msg": "查询成功","data":data,"time":now_time(),"key":""}
    form["num"]=len(form["data"])
    return jsonify(form)

def sql_log():
    sql = "INSERT INTO log(uuid,event,hospital) VALUES (%s,%s,%s)"
    opm = OPMysql()
    resdata = opm.op_list(sql, [str(uuid.uuid1()), str(uuid.uuid1()), str(uuid.uuid1())])
    opm.dispose()


def bytesToHexString(bs):  # 字节转16进制
    # hex_str = ''
    # for item in bs:
    #     hex_str += str(hex(item))[2:].zfill(2).upper() + " "
    # return hex_str
    return ''.join(['%02X ' % b for b in bs])


def hexStringTobytes(str):  # 16进制转字节
    str = str.replace(" ", "")
    return bytes.fromhex(str)


def get_nonce_str():
    '''
    获取随机字符串
    :return:
    '''
    return str(uuid.uuid4()).replace('-', '')


# 列表排序
def takeSecond(elem, val):
    return elem[val]


# ItemCF算法
def ItemSimilarity(train):
    C = dict()
    N = dict()
    for u,items in train.items():
        for i in items.keys():
            N[i] += 1
            for j in items.keys():
                if i == j:
                    continue
                C[i][j] += 1
    W = dict()
    for i,related_items in C.items():
        for j,cij in related_items.items():
            W[i][j] = cij / math.sqrt( N[i] * N[j])
    return W


#根据val值排序
def sort_dict(dict_words):
    """
    字典排序
    :param dict_words:
    :return:
    """
    keys = dict_words.keys()
    values = dict_words.values()

    list_one = [(key, val) for key, val in zip(keys, values)]
    list_sort = sorted(list_one, key=lambda x: x[1], reverse=True)
    fict={}
    for row in list_sort:
        fict[row[0]]=row[1]
    return fict