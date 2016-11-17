import sys
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root',passwd='123456')
conn.select_db('pythontest');
cursor = conn.cursor()
cursor.execute("select * from test")
data = cursor.fetchone()
cursor.close()
conn.close()
print data[1]