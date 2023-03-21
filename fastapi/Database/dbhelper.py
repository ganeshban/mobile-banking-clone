import sqlite3


def sql(sqlStatement:str):
    if not sqlStatement:
        return 'Query not parse'

    try:
        con= sqlite3.connect('mydb.db')
        cur=con.cursor()
        cur.execute(sqlStatement)
        data = cur.fetchall()
        return data,cur.rowcount
    except Exception as e:
        return e
    finally:
        print(cur.rowcount)
        con.commit()
        con.close()

def run_query(sqlstatement:str):
    return sql(sqlstatement)

