# from app import app
# from mysql.connector import connect
# from flask import jsonify
# from flask_cors import CORS
# from util import convertTODict

# conn = connect(
#     user="root",
#     password="password",
#     host="localhost",
#     database="tcs"
# )

# CORS(app, resources={r"/application_details": {"origins": "http://localhost:3000"}})  # Allow requests from http://localhost:3000

# @app.route('/application_details', methods=['GET'])
# def get_app_details():
#     # cursor = None
#     try:
#         cursor = conn.cursor()
#         query = "SELECT * FROM APPLICATION_DETAILS_TABLE"
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         columnName = cursor.description
#         res = convertTODict(columnName, rows)

#         app_name_list = [row["APP_NAME"] for row in res]
#         cursor.close()
#         # conn.close()
#         return jsonify(app_name_list)
#     except Exception as e:
#         return jsonify({'error': str(e)})


from app import app
from flask import jsonify
from flask_cors import CORS
from util import convertTODict
from db import pool

# Create a connection pool for MySQL connections

# Enable CORS for your Flask app
CORS(app, resources={r"/application_details": {"origins": "http://localhost:3000"}})

# Define route to retrieve application details
@app.route('/application_details', methods=['GET'])
def get_app_details():
    try:
        conn = pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM APPLICATION_DETAILS_TABLE"
        cursor.execute(query)
        rows = cursor.fetchall()
        app_name_list = [row["APP_NAME"] for row in rows]
        return jsonify(app_name_list)
 
    
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

    
    
    


# import cx_Oracle
# from flask import Flask, jsonify
# from app import app

# # Connection string
# conStr = 'system/system@localhost:1521/xepdb1'

# # app = Flask(__name__) -> this is INSTANCE, if we want all files to run from "app.py" we should not create new instance and only run from one
# # instance which is declared on app.py

# # CORS(app)

# @app.route('/applications_details', methods=['GET'])
# def get_app_details():
#     with cx_Oracle.connect(conStr) as conn:
#         cur = conn.cursor()
#         cur.execute('select * from "test1".APPLICATION_DETAILS_TABLE')
#         rows = cur.fetchall()
#         app_names = [row[0] for row in rows]
#         return jsonify(app_names)

# if __name__ == '__main__':
#     app.run()

# sqlTxt = 'insert into "test1".APPLICATION_DETAILS_TABLE (APP_NAME, APP_SERVER_HOST, APP_VERSION, APP_SUBVERSION, APP_FILE_SERVER_HOST, APP_FILE_SERVER_TYPE, APP_FILE_SERVER_VERSION, APP_DB_SERVER_HOST, APP_DB_SERVER_TYPE, APP_DB_SERVER_VERSION, APP_IDENTIFIER, APP_ENV) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)'
# dataTuples = [('Oracle Agile PLM', "Server1", 	"1.0", 	"1.0", 	"FileServer1", 	"FileServerType1", "1.0", 	"DBServer1", 	"DBServerType1", 	"1.0", 	"APP1", 	"ENV1"),
#               ('R&D', "Server2", 	"2.0", 	"2.0", 	"FileServer1", 	"FileServerType1", "2.0", 	"DBServer2", 	"DBServerType2", 	"2.0", 	"APP2", 	"ENV2"),
#               ('ADAPTIVE', "Server3", 	"3.0", 	"3.0", 	"FileServer3", 	"FileServerType3", "3.0", 	"DBServer3", 	"DBServerType3", 	"3.0", 	"APP3", 	"ENV3"),
#               ('MATLAB', "Server4", 	"4.0", 	"4.0", 	"FileServer4", 	"FileServerType4", "4.0", 	"DBServer4", 	"DBServerType4", 	"4.0", 	"APP4", 	"ENV4"),]
# cur.executemany(sqlTxt, dataTuples)

# # # cur.executemany(sqlTxt, dataTuples)
# # # print("number of rows inserted = ", cur.rowcount)
# # # conn.commit()


# # if __name__ == '__main__':
# #     app.run()

