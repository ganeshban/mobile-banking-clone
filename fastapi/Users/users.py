from fastapi import APIRouter, Path, Query,Body

from model.user import Users
from core.core import json_data
myUsers=[]
r=APIRouter(prefix='/users',tags=['User'])



@r.get('/login')
def login(
username:str=Query(default=None, title='User Name',description='Enter a User Name for login',min_length=5),
password:str=Query(default=None, title='Password',description='Enter a Password for login',min_length=5)
):
    return json_data({'username':username,'password':password,'token_id':'iadhfiadufhiadfhiahda'})


@r.get('/{userid}')
def get_user(
userid:int=Path(default=None, title='User id',description='Enter a User ID On URL to get user information',gt=0),
):
    return json_data({'username':userid})



@r.post('/create')
def create_user(user:Users):
    return json_data( user)



@r.delete('/delete/{user}')
def delete_user(user:int=Path(default=None,title='UserID', description='Enter a Userid to delete',gt=0)):
    return user

@r.put('/update/{userid}')
def update_user(userid:int=Path(title='UserID',description='Pass the user id on URL to update'), data:Users=Body(title='Update user',description='Pass the required field to update')):
    myData={'userid':userid,'updates':data}
    return json_data(myData)


