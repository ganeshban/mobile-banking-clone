from fastapi import APIRouter, Path, Query,Body

from model.user import Users
from core.core import DB_Table, json_data

table=DB_Table('tblusers','userid')
r=APIRouter(prefix='/users',tags=['User'])


@r.get('/{userid}')
def get_user(
userid:int=Path(default=None, title='User id',description='Enter a User ID On URL to get user information',gt=0),
):
    res,metadata = table.get_one(userid)
    return json_data(Users.from_list(res),meta=metadata)

@r.post('/create')
def create_user(user:Users):
    res,_=table.save_to_database(user.dict())
    return json_data(res,meta=_)



@r.delete('/delete/{user}')
def delete_user(user:int=Path(default=None,title='UserID', description='Enter a Userid to delete',gt=0)):
    res,mdata=table.delete_from_database(user)
    data=mdata.get('msg',f'user having id {user} is deleted.')
    mdata['msg']=data
    return json_data( res,meta=mdata)

@r.put('/update/{userid}')
def update_user(
userid:int=Path(title='UserID',description='Pass the user id on URL to update'), 
source:Users=Body(title='Update user',description='Pass the required field to update')
):
    res,mdata=table.update_to_database(source.dict(), userid)
    data=mdata.get('msg','user updated successfully')
    mdata['msg']=data
    return json_data(res, meta=mdata)


