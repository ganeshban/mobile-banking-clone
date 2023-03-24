from fastapi import APIRouter, Path, Query,Body

from model.account import Account as account
from core.core import json_data,DB_Table

table=DB_Table('tblAccounts','accountid')
r=APIRouter(prefix='/account',tags=['Account'])

@r.get('/list/{userid}')
def get_list_account(
userid:int=Path(default=None, title='User id',description='Enter a User ID On URL to get user Accounts',gt=0),
):
    result,mdata=table.custom_query(f'select * from tblaccounts where userID = {userid}')
    if type(result) is list:
        return json_data(account.from_list(result),meta=mdata)
    return json_data(result,meta=mdata)

@r.get('/{accountid}')
def get_account(
accountid:str=Query(default=None, title='Account ID',description='Enter a Account ID ',min_length=5),
):
    result,m = table.get_one(accountid)
    if type(result) is list:
        return json_data(account.from_list(result), meta=m)
    return json_data(result,meta=m)

@r.post('/create')
def create_account(data:account):
    res,met=table.save_to_database(data.dict())
    if type(res)==str:
        return json_data(res,meta=met)
    return json_data(account.from_list(res),meta=met)

@r.delete('/delete/{accountid}')
def delete_account(
accountid:str=Path(default=None,title='Account ID', description='Enter a Account ID to delete')
):
    res,mdata=table.delete_from_database(accountid)
    data=mdata.get('msg',f'Account having id {accountid} is deleted.')
    mdata['msg']=data
    return json_data( res,meta=mdata)

@r.put('/update/{accountid}')
def update_account(
accountid:int=Path(title='accountID',description='Pass the account id on URL to update'), 
source:account=Body(title='Update account',description='Pass the required field to update')
):
    res,mdata=table.update_to_database(source.dict(), accountid)
    data=mdata.get('msg','Record Updated succesfully')
    mdata['msg']=data
    return json_data(res,meta=mdata)
