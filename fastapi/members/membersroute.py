from fastapi import APIRouter, Path, Query


from model.members import Members, MembersList
from core.core import json_data


r=APIRouter(prefix='/members',tags=['Members'])


@r.get('/list')
def get_member_list(
field:str=Query(default='', title='Member Serial Number',description='Enter a members serial number to get members infomartion'),
val:str=Query(default='', title='Member Serial Number',description='Enter a members serial number to get members infomartion')
):
    data=''
    if not field is None:
        data+=field
    if not val is None:
        data+=val
    return json_data({'field':data,'lst':MembersList})


@r.get('/{memsn}')
def get_member(
memsn:int=Path(default=None, title='Member Serial Number',description='Enter a members serial number to get members infomartion',gt=0),
):
    return json_data(MembersList[memsn])


@r.post('/new')
def create_member(member:Members):
    MembersList.append(member)
    return json_data( member)


@r.post('/update/{memsn}')
def update_member(memsn:int,member:Members):
    MembersList[memsn]=member
    return json_data( member)


@r.delete('/delete/{memsn}')
def delete_member(memsn:int):
    MembersList.pop(memsn)
    return json_data( {'message':'members deleted success'})

