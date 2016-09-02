import MySQLdb
db = MySQLdb.connect("localhost","root","candy1991","mysql")
cursor = db.cursor()
cursor.execute("select * from user")
data = cursor.fetchone()
print data
