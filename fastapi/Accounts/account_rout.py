from fastapi import APIRouter, Path, Query,Body

from model.account import Account as account
from core.core import json_data,DB_Table

table=DB_Table('tblAccounts')
r=APIRouter(prefix='/account',tags=['Account'])


@r.get('/list/{userid}')
def get_list_account(
userid:int=Path(default=None, title='User id',description='Enter a User ID On URL to get user Accounts',gt=0),
):
    a=table.run_query(f'Select * from tblAccounts where user = {userid}')
    if type(a) is list:
        return json_data(account.from_list(a))
    return json_data(a,error=1)


@r.get('/{accountid}')
def get_account(
accountid:str=Query(default=None, title='Account ID',description='Enter a Account ID ',min_length=5),
):
    acc = table.get_one(accountid)
    if type(acc) is list:
        return json_data(acc)
    return json_data(acc,error=1)





@r.post('/create')
def create_account(data:account):

    a=table.save_to_database(data.dict())
    return json_data(a)


@r.delete('/delete/{accountid}')
def delete_account(
accountid:str=Path(default=None,title='Account ID', description='Enter a Account ID to delete')
):
    acc=table.delete_from_database(accountid)
    data=''
    if acc:
        data=acc
    else:
        data=f'Account having id {accountid} is deleted.'
    return json_data( data)



@r.put('/update/{accountid}')
def update_account(
accountid:int=Path(title='accountID',description='Pass the account id on URL to update'), 
data:account=Body(title='Update account',description='Pass the required field to update')
):
    new_acc=table.update_to_database(data.dict(), accountid)
    if new_acc:
        return json_data({'msg':'Update failed ','details':new_acc}, error=1)
    return json_data('Record Updated succesfully')


