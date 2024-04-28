# -*- coding:utf-8 -*-
import datetime
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb
db_operater = MySQLdb.connect("127.0.0.1", "root", "22", "database", charset='utf8')
db_cursor = db_operater.cursor()
with open("d:/data.sql", "rb") as f:
    sql = f.readlines()
sql = "".join(sql)
s_list = [i.start() for i in re.finditer('insert into', sql)]
s_len = len(s_list)
for index, pos in enumerate(s_list):
    if index < s_len - 1:
        curr_sql = sql[pos:s_list[index+1]]
    else:
        curr_sql = sql[pos:]
    try:
        db_cursor.execute(curr_sql)
        db_operater.commit()
    except:
        db_operater.rollback()
db_cursor.close()