from fastapi import FastAPI #,Depends
from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer

import Users.users as u
import Accounts.account_rout as a
import Transaction.transaction_rout as t
from core.core import DB_Table, json_data
import members.membersroute as m





# oauth=OAuth2PasswordBearer(tokenUrl='hello')
# app=FastAPI(title='MobBankingApi',version='0.0.1',dependencies=[Depends(oauth)])
app=FastAPI(title='MobBankingApi',version='0.0.1')
app.include_router( u.r)
app.include_router( t.r)
app.include_router( m.r)
app.include_router( a.r)

table=DB_Table('')
class CustomQry(BaseModel):
    q:str=''

@app.post('/custom')
def my_qry(qry:CustomQry):
    sql=str(qry)
    sql=sql.removeprefix("q='")
    sql=sql.removesuffix("'")
    result=table.custom_query(sql)
    return json_data(result)