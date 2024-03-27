from app import app  # Import the existing Flask app instance
import cx_Oracle
from flask import jsonify
from flask_cors import CORS

conStr = 'system/system@localhost:1521/xepdb1'
CORS(app, resources={r"/server_status": {"origins": "http://localhost:3000"}})  # Allow requests from http://localhost:3000

conn = cx_Oracle.connect(conStr)

@app.route('/server_status', methods=['GET'])
def get_server_status():
    cur = conn.cursor()
    cur.execute('select * from "test1".SERVER_STATUS_TABLE')
    rows = cur.fetchall()
    cur.close()

    server_status = []
    for row in rows:
        status = {
            'SERVER_RESPONSE_CODE': row[0],
            'EXEC_TIME': row[2],
        }
        server_status.append(status)

    return jsonify(server_status)

if __name__ == '__main__':
    app.run()

    
# cur.execute('''
#     CREATE TABLE "test1".SERVER_STATUS_TABLE (
#         SERVER_RESPONSE_CODE VARCHAR2(20 BYTE),
#         EXEC_DATE VARCHAR2(20 BYTE),
#         EXEC_TIME VARCHAR2(20 BYTE),
#         APP_IDENTIFIER VARCHAR2(20 BYTE),
#         HOSTNAME VARCHAR2(30 BYTE),
#         ALERT_FLAG VARCHAR2(20 BYTE),
#         ALERT_SEVERITY VARCHAR2(20 BYTE)
#     )'''
# )

# SERVER_RESPONSE_CODE,EXEC_TIME

# sqlTxt = 'insert into "test1".SERVER_STATUS_TABLE(SERVER_RESPONSE_CODE,EXEC_DATE,EXEC_TIME,APP_IDENTIFIER,HOSTNAME,ALERT_FLAG,ALERT_SEVERITY) values (:1,:2,:3,:4,:5,:6,:7)'

# dataTuples = [("200", "03-15-2024", "00:15", "ODBC ", "localhost", "N", "N"),
#               ("200", "01-20-2024", "00:37", "ODBC ", "localhost", "N", "N"),
#               ("400", "07-17-2023", "00:40", "ODBC ", "localhost", "N", "N"),
#               ("200", "10-07-2023", "00:20", "ODBC ", "localhost", "N", "N")]
# # MAIN COLUMN -> EXEC_TIME(x-axis) SERVER_RESPONSE_CODE(y-axis)
# cur.executemany(sqlTxt,dataTuples)
# print("No of rows affected " + str(cur.rowcount))

if __name__ == '__main__':
  app.run()
