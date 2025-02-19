import pymysql
def connect_db():
    try:
        connection = pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='shashi_db',charset='utf8')
        print("DB connected")
        return connection   
    except:
        print("DB connected failed")

def disconnect_db(connection):
    try:
        connection.close()
        print("DB disconnected")
    except:
        print("Error in disconnection")

def create_db():
    connection = connect_db()
    query = 'create database IF NOT EXISTS shashi_db;'
    cursor = connection.cursor()
    cursor.execute(query)
    disconnect_db(connection)

def insert_row():
    connection=connect_db()
c=connect_db()
if c:
    disconnect_db(c)
create_db()