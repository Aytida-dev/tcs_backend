from mysql.connector import connect

conn = connect(
  user = "root",
  password = "password",
  host= "localhost",
  database = "tcs"
)

def callDB(query):
    mycursor = conn.cursor()
    mycursor.execute(query)
    res = mycursor.fetchall()
    column_names = [i[0] for i in mycursor.description] 
    result_with_column_names = []
    for row in res:
        result_with_column_names.append(dict(zip(column_names, row)))
    return result_with_column_names

def closeConn():
  conn.close()