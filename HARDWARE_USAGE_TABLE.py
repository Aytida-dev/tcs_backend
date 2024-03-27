import cx_Oracle

conStr = 'system/system@localhost:1521/xepdb1'

conn = cx_Oracle.connect(conStr)
cursor = conn.cursor()

create_table_sql = """
    CREATE TABLE "test1".HARDWARE_USAGE_TABLE (
        COMPONENT VARCHAR2(20 BYTE),
        TYPE VARCHAR2(20 BYTE),
        TOTAL_ALLOC VARCHAR2(20 BYTE),
        TOTAL_USAGE VARCHAR2(20 BYTE),
        FREE_ALLOC VARCHAR2(20 BYTE),
        EXEC_DATE VARCHAR2(20 BYTE),
        EXEC_TIME VARCHAR2(20 BYTE),
        APP_IDENTIFIER VARCHAR2(30 BYTE),
        HOSTNAME VARCHAR2(20 BYTE),
        ALERT_FLAG VARCHAR2(20 BYTE)
    )
"""

cursor.execute(create_table_sql)

conn.commit()

cursor.close()
conn.close()
