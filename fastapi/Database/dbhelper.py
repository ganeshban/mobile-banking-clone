import sqlite3
# import pyodbc


def sql(sqlStatement:str):
    if not sqlStatement:
        return 'Query not parse',0

    try:
        con= sqlite3.connect('mydb.db')
        cur=con.cursor()
        cur.execute(sqlStatement)
        data = cur.fetchall()
        return data, cur.rowcount
    except Exception as e:
        return str(e),0
    finally:
        con.commit()
        con.close()


# def sql(sqlStatement:str):
#     if not sqlStatement:
#         return 'Query not parse',0

#     try:
#         con= pyodbc.connect('''
#         DRIVER={Devart ODBC Driver for SQL Server};
#         Server=LAPTOP-DL9406IV;
#         Database=master;
#         Trusted_Connection=yes;
#         ''')


#          #Database=mydatabase;Port=myport;User ID=myuserid;Password=mypassword')

#         cur=con.cursor()
#         cur.execute(sqlStatement)
#         data = cur.fetchall()
#         return data, cur.rowcount
#     except Exception as e:
#         return str(e),0
#     finally:
#         # con.commit()
#         # con.close()
#         pass

def run_query(sqlstatement:str):
    return sql(sqlstatement)

