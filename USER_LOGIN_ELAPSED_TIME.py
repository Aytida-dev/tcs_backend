from app import app
from db import callDB
from flask import jsonify
from flask_cors import CORS

CORS(app, resources={r"/user_login_elapsed_time": {"origins": "http://localhost:3000"}})  # Allow requests from http://localhost:3000

@app.route('/user_login_elapsed_time' , methods=['GET'])
def get_user_login_elapsed_time():
    try:
        query = "SELECT * FROM USER_LOGIN_ELAPSED_TIME"
        res = callDB(query)
        server_status_res = []
        
        for row in res:
            dict = {
                    "ELAPSED_TIME" : row["ELAPSED_TIME"], 
                    "EXEC_TIME" : row["EXEC_TIME"]
                }
            
            server_status_res.append(dict)
        
        return jsonify(server_status_res)
    except Exception as e:
        return jsonify({'error': str(e)}) 


# from app import app
# import cx_Oracle
# from flask import Flask, jsonify

# # Define your routes and other configurations for this blueprint


# conn = cx_Oracle.connect('system/system@localhost:1521/xepdb1')

# @app.route('/user_login_elapsed_time', methods=['GET'])
# def get_user_login_elapsed_time():
#   cur = conn.cursor()
  
#   cur.execute('select * from "test1".USER_LOGIN_ELAPSED_TIME')
  
#   rows = cur.fetchall()
  
#   cur.close()
  
#   login_time = []
  
#   for row in rows:
#     login = {
#       'ELAPSED_TIME' : row[0],
#       'EXEC_TIME' : row[2],
#     }
#     login_time.append(login)
    
#   print(login_time)
#   return jsonify(login_time)

# # cur.execute('''
# #     CREATE TABLE "test1".USER_LOGIN_ELAPSED_TIME (
# #         ELAPSED_TIME VARCHAR2(20 BYTE),
# #         EXEC_DATE VARCHAR2(20 BYTE),
# #         EXEC_TIME VARCHAR2(20 BYTE),
# #         APP_IDENTIFIER VARCHAR2(20 BYTE),
# #         ALERT_FLAG VARCHAR2(20 BYTE),
# #         ALERT_SEVERITY VARCHAR2(20 BYTE)
# #     )
# # ''')

# # sqlTxt = 'insert into "test1".USER_LOGIN_ELAPSED_TIME (ELAPSED_TIME, EXEC_DATE, EXEC_TIME, APP_IDENTIFIER, ALERT_FLAG, ALERT_SEVERITY) values (:1,:2,:3,:4,:5,:6)'
# # dataTuples = [('7', "03:15:00", 	"0.25", "N", "N", "N"),
# #               ('10', "11:25:00", 	"0.5", "N", "N", "N"),
# #               ('12', "07:40:00", 	"0.75", "N", "N", "N"),
# #               ('16', "09:30:00", 	"5.00", "N", "N", "N")]
# # # MAIN COLUMN - EXEC_TIME(x-axis) ELAPSED TIME(y-axis)

# # cur.executemany(sqlTxt, dataTuples)
# # print("No. of rows affected: " + str(cur.rowcount))


# if __name__ == '__main__':
#   app.run()
