
from fastapi import FastAPI ,Depends, Query
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

from rout import account, login, members, transaction,users
from core.core import DB_Table, json_data





# oauth=OAuth2PasswordBearer(tokenUrl='users/login')
oauth=OAuth2PasswordBearer(tokenUrl='token')
app=FastAPI(title='MobBankingApi',version='0.0.1')

auth=[Depends(oauth)]

def register_rout(rout,use_auth=auth):    
    app.include_router( rout,dependencies=use_auth)

register_rout( account.r)
register_rout(login.r,None)
register_rout( members.r)
register_rout( transaction.r)
register_rout( users.r)

table=DB_Table('')
class CustomQry(BaseModel):
    q:str=''

@app.post('/custom',dependencies=auth)
def my_qry(qry:CustomQry):
    sql=str(qry.q)
    result=table.custom_query(sql)
    return json_data(result)
