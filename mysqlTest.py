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
sql = "select host,user from user"
cursor.execute(sql)
for a,b in cursor.fetchall():
	print(a,b)
