from fastapi import APIRouter, Path, Query,Body

from model.account import Account
from core.core import json_data

r=APIRouter(prefix='/account',tags=['Account'])

@r.get('/list/{userid}')
def get_list_account(
userid:int=Path(default=None, title='User id',description='Enter a User ID On URL to get user Accounts',gt=0),
):
    return json_data({'title':f' accounts of {userid}'})


@r.get('/{accountid}')
def get_account(
accountid:str=Query(default=None, title='Account ID',description='Enter a Account ID ',min_length=5),
):
    return json_data({'accountname':'will return account'})





@r.post('/create')
def create_account(account:Account):
    return json_data( account)


@r.delete('/delete/{accountid}')
def delete_account(
accountid:str=Path(default=None,title='Account ID', description='Enter a Account ID to delete')
):
    return json_data( accountid)

@r.put('/update/{accountid}')
def update_account(
accountid:int=Path(title='accountID',description='Pass the account id on URL to update'), 
data:Account=Body(title='Update account',description='Pass the required field to update')
):
    myData={'accountid':accountid,'updates':data}
    return json_data(myData)


