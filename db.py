def dbUsage(unamegiven , passwordgiven):
	import sqlite3

	connection=sqlite3.connect("mydb.db")

	crsr=connection.cursor()

	sql_command="""CREATE TABLE users (
	uname VARCHAR(30) PRIMARY KEY,
	password VARCHAR(30)
	);"""

	crsr.execute(sql_command)

	sql_command="""INSERT INTO users VALUES("Vishwanath","vishu");"""
	crsr.execute(sql_command)
	sql_command="""INSERT INTO users VALUES("Sarthak","sarthak");"""
	crsr.execute(sql_command)
	sql_command="""INSERT INTO users VALUES("Kunal","kunal");"""
	crsr.execute(sql_command)

	#unamegiven="Sarthak"
	#print(type(unamegiven))
	#passwordgiven=str("vishu")

	def convertTuple(tup):
		str=''.join(tup)
		return str


	pyuname="SELECT password FROM users WHERE uname = ?"
	crsr.execute(pyuname,(unamegiven,))
	values1=crsr.fetchall()
	finalpassword=values1[0]
	str=convertTuple(finalpassword)
	if passwordgiven==str:
		print("true")
	else:
		print("false")


	connection.commit()

	connection.close()