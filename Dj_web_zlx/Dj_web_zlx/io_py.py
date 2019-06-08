import pymysql
from snownlp import SnowNLP

#连接MySQL的模块
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='zhenglixin', port=3306, charset='utf8')
#与mysql建立连接
cur = conn.cursor()
#操作游标
sql1="select a.goodsId,rateContent from tianmao_goods_comments a inner join tianmao_goods b where a.goodsId=b.goodsId and a.rateContent is not null"
cur.execute("USE zhenglixin")
cur.execute(sql1)
#执行sql语句
tup1=cur.fetchall()
#数据库的信息读取出来放入一个元组
#print(type(tup1))
for i in tup1:
    #遍历拿到每一行的数据 将每一行的元组修改为列表 元组不能修改长度
    list2=list(i)
    #将每条评论i[1]的情感值添加到该列表即
    #print(i[1]) #产生一个数值
    try:
        emotion=SnowNLP(list2[1]).sentiments
    except:
        print("被除数不能为零")
    #这里不加异常处理会除数为零的异常
    list2.append(emotion)
    print(list2)
    #商品id,商品的评论,情感值
    sql2= "insert into emotion(goodsId,rateContent,emotion) values(%s, %s, %s)"
    values = (list2[0],list2[1],list2[2])
#将新得到的数据插入到mysql的表中
    cur.execute(sql2,values)
conn.commit()
cur.close()
conn.close()
#提交并关闭连接
