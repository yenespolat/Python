import mysql.connector as sqlcon

db = sqlcon.connect(
    host='localhost',
    user='root',
    password='admin',
    database='eaccountant'
)


def add_user(username, password):
    cursor = db.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(sql, (username, password))
    db.commit()
    cursor.close()
    return True

def get_user(username):      
    cursor = db.cursor()
    uname = (username,)
    cursor.execute("SELECT * FROM users WHERE username=%s", uname)
    result = cursor.fetchone()
    cursor.close()
    return result