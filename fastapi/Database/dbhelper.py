import pyodbc

conn = pyodbc.connect('''DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-DL9406IV\MSSQLSERVER01;
DATABASE=KpiReport;
UID=sa;
PWD=password'''
)

# user