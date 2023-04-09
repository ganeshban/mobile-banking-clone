from fastapi import FastAPI ,Depends, Query
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

import Users.users as u
import Accounts.account_rout as a
import Transaction.transaction_rout as t
from core.core import DB_Table, json_data
import members.membersroute as m
from model.user import Users





oauth=OAuth2PasswordBearer(tokenUrl='users/login')
app=FastAPI(title='MobBankingApi',version='0.0.1')

auth=[Depends(oauth)]

def register_rout(rout):    
    app.include_router( rout,dependencies=auth)

register_rout( u.r)
register_rout( t.r)
register_rout( m.r)
register_rout( a.r)

table=DB_Table('')
class CustomQry(BaseModel):
    q:str=''

@app.post('/custom',dependencies=auth)
def my_qry(qry:CustomQry):
    sql=str(qry.q)
    result=table.custom_query(sql)
    return json_data(result)

@app.get('/login',tags=['User'])
def login(
username:str=Query(default='', title='User Name',description='Enter a User Name for login',min_length=5),
password:str=Query(default='', title='Password',description='Enter a Password for login',min_length=5),
auth_code:str=Query(default=None)):
    # return json_data({'username':username,'password':password,'token_id':'iadhfiadufhiadfhiahda'})

    where=f" where username = '{username}' and userpassword = '{password}' "
    result,_=table.get_all(where)
    if type(result) is list and len(result)>0:
        return json_data(Users.from_list(result),meta=_)
    return json_data('either username or password is wrong.',meta=_)

