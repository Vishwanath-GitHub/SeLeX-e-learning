def sql_register(uname, password):
    import sqlite3

    connection = sqlite3.connect("mydb.db")

    crsr = connection.cursor()
    def convertTuple(tup):
        s = ''.join(tup)
        return s
    u = str(uname)
    sqlcheck = "SELECT uname FROM users WHERE uname =?"
    crsr.execute(sqlcheck, (u,))
    values2 = crsr.fetchall()
    print(values2)
    if values2 == []:
        sql_command = """INSERT INTO users VALUES(?,?);"""
        crsr.execute(sql_command, (uname, password,))
        print("It is Working!")
        connection.commit()
        connection.close()
        return True
    else:
        username = values2[0]
        s = convertTuple(username)
        connection.commit()
        connection.close()
        if s == u:
            return False





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
