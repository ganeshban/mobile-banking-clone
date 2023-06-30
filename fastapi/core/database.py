import sqlite3
import pyodbc


def connect_sqlite3(sqlStatement: str):
    if not sqlStatement:
        return 'Query not parse', 0
    try:
        con = sqlite3.connect('mydb.db')
        cur = con.cursor()
        cur.execute(sqlStatement)
        data = cur.fetchall()
        return data, cur.rowcount
    except Exception as e:
        return str(e), 0
    finally:
        con.commit()
        con.close()


def connect_sql_server(sqlStatement: str):
    if not sqlStatement:
        return 'Query not parse', 0
    try:
        SERVER = "localhost\GANESH"
        DB = "user"
        USERID = "SA"
        PASSWORD = "123"
        STR = f"DRIVER={{{pyodbc.drivers()[-1]}}}; SERVER={SERVER}; DATABASE={DB}; UID={USERID}; PWD={PASSWORD};"
        con = pyodbc.connect(STR)
        cur = con.cursor()
        cur.execute(sqlStatement)
        data = cur.fetchall()
        return data, cur.rowcount
    except Exception as e:
        return str(e), 0
    finally:
        if con:
            con.commit()
            con.close()


SQLITE = "SQLITE"
SQLSERVER = "SQLSERVER"


def sql(sqlqry: str, database: str = "SQLITE"):
    cur_db = database
    cur_db = SQLSERVER
    data = None
    if cur_db == SQLITE:
        data = connect_sqlite3(sqlqry)
    elif cur_db == SQLSERVER:
        data = connect_sql_server(sqlqry)
    return data


def run_query(sqlstatement: str):
    return sql(sqlstatement)


# a = run_query("select * from sysobjects ")
# print(a)
