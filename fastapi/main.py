from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer

import Users.users as u
import Accounts.account_rout as a
import Transaction.transaction_rout as t
import members.membersroute as m

# oauth=OAuth2PasswordBearer(tokenUrl='hello')
# app=FastAPI(title='MobBankingApi',version='0.0.1',dependencies=[Depends(oauth)])
app=FastAPI(title='MobBankingApi',version='0.0.1')
app.include_router( u.r)
app.include_router( a.r)
app.include_router( t.r)
app.include_router( m.r)