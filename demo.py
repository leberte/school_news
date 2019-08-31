# encoding: utf-8
from Helpermysql import MysqlHelper
from spider import *
from sendmail import *
import os


info = get_yanghau() +vatuu()+ get_new_yanghau()+ tumu()
x = []
for i in info:
    x.append(i[0])
x1 = set(x)

sql = MysqlHelper()
try:
    sql.connect()
    sql.close()
except :
    pass

sql_result = []
for j in list(x1):
    order = "SELECT url FROM school WHERE time = %s"
    parama = (j,)
    sql_result.append(sql.get_all(order,parama))

sql_result_final = []
for i in sql_result:
    sql_result_final += i

result = []
for i in info:
    if i[1] not in sql_result_final:
        result.append(i)
    else:
        continue
if result != []:
    for item in result:
        order2 = "INSERT INTO school(time,url,title) VALUES (%s,%s,%s)"
        parama2 = (item[0],item[1],item[2])
        sql.insert(order2,parama2)
    mail_message(result)
    print("有更新！")
    context = '学校更新下面通知啦~'
#    for i in result:
#       context += i[2] + i[1]+"发布时间为:"+ i[0]
#    os.system("qq send group 土木四班水群 %s"%context)
 #   os.system("qq send group SWJTU-铁道2018-4班 %s"%context)
else:
    print('无更新！')
    pass
print('success!')
