from app import app
from flask import Flask, request, jsonify
import cx_Oracle
import json
from flask_cors import CORS


conStr = 'system/system@localhost:1521/xepdb1'
# CORS(app, resources={r"/maxValue": {"origins": "*"}})
CORS(app, resources={r"/maxValue": {"origins": "http://localhost:3000"}}) 
CORS(app, resources={r"/maxValueGraph": {"origins": "http://localhost:3000"}}) 
CORS(app, resources={r"/test": {"origins": "http://localhost:3000"}}) 

connection = cx_Oracle.connect(conStr)

@app.route('/maxValue', methods=['GET'])
def get_max_value():
    try:
        json_data = request.args.get('jsonData')
        print("Received JSON data:", json_data)  # Add this line for logging

        # Check if JSON data is provided
        if json_data:
            return jsonify({'Data': json_data})
        else:
            return jsonify({'error': 'No JSON data provided'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/maxValueGraph', methods=['GET'])
def get_graph():
    try:
        json_data = request.args.get('jsonData')
        if json_data:
            data_dict = json.loads(json_data)
            value = data_dict.get("ReportValue")
            # return jsonify({'value': value})
            if(value == "Daily Total User Session"):
                cur = connection.cursor()
                cur.execute('select * from "test1".MAX_VALUE_TABLE')
                rows = cur.fetchall()
                row_count = len(rows)  # Count the number of rows fetched
                cur.close()
                print(rows)
                forGraph = []
                
                for row in rows:
                    session = {
                        'MAX_VALUE' : row[2],
                        'EXEC_DATE' : row[1],
                        'EXEC_TIME' : row[3]
                    }
                    forGraph.append(session)
                return jsonify({'rows': forGraph, 'row_count': row_count})
        else:
            return jsonify({'error': 'No JSON data provided'}), 400
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

# @app.route('/test', methods=['GET'])
# def test():
#     cur = connection.cursor()
#     date = "03-15-2024"
#     cur.execute('SELECT * FROM "test1".USER_SESSIONS_TABLE WHERE EXEC_DATE = ? ORDER BY USER_ACTIVE_SESSIONS' , [date])
#     rows = cur.fetchall()
    
#     return jsonify({rows:rows})
    
if __name__ == '__main__':
    app.run(debug=True)
