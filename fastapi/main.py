from fastapi import FastAPI
from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer

import Users.users as u
import Accounts.account_rout as a
import Transaction.transaction_rout as t
import members.membersroute as m
from  database.dbhelper import run_query
# oauth=OAuth2PasswordBearer(tokenUrl='hello')
# app=FastAPI(title='MobBankingApi',version='0.0.1',dependencies=[Depends(oauth)])
app=FastAPI(title='MobBankingApi',version='0.0.1')
app.include_router( u.r)
app.include_router( t.r)
app.include_router( m.r)
app.include_router( a.r)

class QryCls(BaseModel):
    q:str

@app.post('/custom')
def custom(qry:QryCls):
    a=run_query(qry)
    return a