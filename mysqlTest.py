import pymysql
connect = pymysql.Connect(
	host = 'localhost',
	port=3306,
	user='root',
	passwd='root',
	db='mysql',
	charset='utf8'
)
cursor = connect.cursor()
sql = "select * from user"
cursor.execute(sql)
for row in cursor.fetchall():
	print(row)
