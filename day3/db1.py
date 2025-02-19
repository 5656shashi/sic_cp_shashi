import pymysql
def connect_db():
    try:
        connection = pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='shashi_db',charset='utf8')
        print("DB connected")
    except:
        print("DB connected failed")
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print("DB disconnected")
    except:
        print("Error in disconnection")

c=connect_db()
disconnect_db(c)