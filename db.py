from mysql.connector import connect

conn = connect(
    user="root",
    password="password",
    host="localhost",
    database="tcs"
)

def getCursor():    
    cursor = conn.cursor()
    return cursor

def closeCursor(mycursor):
    mycursor.close()

      
# def callDB(query, data=None):
#     try:
#         mycursor = conn.cursor()

#         if data:
#             mycursor.execute(query, data)
#         else:
#             mycursor.execute(query)

#         res = mycursor.fetchall()

#         column_names = [i[0] for i in mycursor.description] 
#         result_with_column_names = []

#         for row in res:
#             result_with_column_names.append(dict(zip(column_names, row)))
        
#         return result_with_column_names

#     finally:
#         if mycursor:  
#             mycursor.close()  # Close the cursor in the finally block

def closeConn():
    conn.close()


# from mysql.connector import connect

# # Establish a connection to the MySQL database
# conn = connect(
#     user="root",
#     password="password",
#     host="localhost",
#     database="tcs"
# )

# def callDB(query, data=False):
#     mycursor = conn.cursor()
#     try:
#         if data:
#             mycursor.execute(query, data)
#         else:
#             mycursor.execute(query)
        
#         # Fetch all rows and column names
#         res = mycursor.fetchall()
#         column_names = [i[0] for i in mycursor.description]
        
#         # Convert result into a list of dictionaries
#         result_with_column_names = [dict(zip(column_names, row)) for row in res]
        
#         return result_with_column_names
#     finally:
#         # Ensure to consume all results before reusing the cursor
#         while mycursor.nextset():
#             pass

# def closeConn():
#     # Close the database connection
#     conn.close()
