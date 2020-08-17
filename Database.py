
def sql_register(uname, password):
    import sqlite3

    connection = sqlite3.connect("mydb.db")

    crsr = connection.cursor()
    sql_command = """INSERT INTO users VALUES(?,?);"""
    crsr.execute(sql_command, (uname, password,))
    print("It is Working!")
    connection.commit()

    connection.close()


def checker(uname, password):
    import sqlite3

    connection = sqlite3.connect("mydb.db")

    crsr = connection.cursor()
    unamegiven = str(uname)
    passwordgiven = str(password)

    def convertTuple(tup):
        s = ''.join(tup)
        return s

    pyuname = "SELECT password FROM users WHERE uname = ?"
    crsr.execute(pyuname, (unamegiven,))
    values1 = crsr.fetchall()
    finalpassword = values1[0]
    s = convertTuple(finalpassword)
    if passwordgiven == s:
        return True
    else:
        return False

    connection.commit()

    connection.close()
