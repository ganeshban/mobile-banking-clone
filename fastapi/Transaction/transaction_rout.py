from fastapi import APIRouter, Path


from model.transaction import Transaction
from core.core import json_data


r=APIRouter(prefix='/transaction',tags=['Transaction'])



@r.get('/{transID}')
def get_user(
transid:int=Path(default=None, title='User id',description='Enter a User ID On URL to get user information',gt=0),
):
    return json_data({'msg':f' Transaction with the ID {transid} will be here'})



@r.post('/new')
def create_user(trans:Transaction):
    return json_data( trans)

