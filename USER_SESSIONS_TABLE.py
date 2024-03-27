from app import app
from db import callDB
from flask import jsonify
from flask_cors import CORS

CORS(app, resources={r"/user_sessions": {"origins": "*"}})  # Allow requests from http://localhost:3000

@app.route('/user_sessions' , methods=['GET'])
def get_user_session():
    try:
        query = "SELECT * FROM USER_SESSIONS_TABLE"
        res = callDB(query)
        server_status_res = []
        
        for row in res:
            dict = {
                    "USER_ACTIVE_SESSIONS" : row["USER_ACTIVE_SESSIONS"], 
                    "EXEC_TIME" : row["EXEC_TIME"]
                }
            
            server_status_res.append(dict)
        
        return jsonify(server_status_res)
    except Exception as e:
        return jsonify({'error': str(e)});

# from app import app
# import cx_Oracle
# from flask import Flask, jsonify

# # Define your routes and other configurations for this blueprint


# # Connection string
# conStr = 'system/system@localhost:1521/xepdb1'


# conn = cx_Oracle.connect(conStr)

# @app.route('/user_sessions', methods=['GET'])

# def get_user_session():
#   cur = conn.cursor()
  
#   cur.execute('select * from "test1".USER_SESSIONS_TABLE')
  
#   rows = cur.fetchall()
  
#   cur.close()
  
#   user_session = []
  
#   for row in rows:
#     session = {
#       'USER_ACTIVE_SESSIONS' : row[0],
#       'EXEC_TIME' : row[3]
#     }
#     user_session.append(session)
  
#   print(user_session)
#   return jsonify(user_session)

# # sqlTxt = 'insert into "test1".USER_SESSIONS_TABLE (USER_ACTIVE_SESSIONS, USER_TOTAL_SESSIONS, EXEC_DATE, EXEC_TIME, APP_IDENTIFIER) values (:1,:2,:3,:4,:5)'
# # dataTuples = [('100', "03:15:00", 	"03-15-2024", "0.25", "ODBC "),
# #               ('20', "11:25:00", 	"01-15-2024", "0.5", "ODBC "),
# #               ('35', "07:40:00", 	"07-15-2024", "0.75", "ODBC "),
# #               ('5', "09:30:00", 	"015-15-2024", "5.00", "ODBC ")]
# # # MAIN COLUMN - EXEC_TIME(x-axis) USER_TOTAL_SESSIONS(y-axis)

# # cur.executemany(sqlTxt, dataTuples)
# # print("No. of rows affected: " + str(cur.rowcount))

# if __name__ == '__main__':
#   app.run()