from fastapi import APIRouter, Path, Query

from model.members import Members as member
from core.core import json_data, DB_Table

table=DB_Table('tblmembers')
r=APIRouter(prefix='/members',tags=['Members'])

@r.get('/list')
def get_member_list(
wherecluse:str=Query(default=None, title='Member Serial Number',description='Enter a members serial number to get members infomartion'),
orderby:str=Query(default=None, title='Member Serial Number',description='Enter a members serial number to get members infomartion')
):
    data=''
    if wherecluse:
        data=f' where {wherecluse}'
    if orderby:
        data+=f' order by {orderby}'
    result,_=table.get_all(data)#,f"Select * from tblmembers {data} ")
    if type(result) is list:
        return json_data(member.from_list(result),meta=_)
    return json_data(result,meta=_)

@r.get('/{memsn}')
def get_member(
memsn:int=Path(default=None, title='Member Serial Number',description='Enter a members serial number to get members infomartion',gt=0),
):
    
    mem,metadata = table.get_one(memsn)
    return json_data(member.from_list(mem),meta=metadata)


@r.post('/new')
def create_member(newmem:member):
    a,_=table.save_to_database(newmem.dict())
    return json_data(a,meta=_)


@r.post('/update/{memsn}')
def update_member(memsn:int,newmem:member):
    res,mdata=table.update_to_database(newmem.dict(), memsn)
    data=mdata.get('msg','Member updated successfully')
    mdata['msg']=data
    return json_data(res, meta=mdata)

@r.delete('/delete/{memsn}')
def delete_member(memsn:int):
    res,mdata=table.delete_from_database(memsn)
    data=mdata.get('msg',f'Member having id {memsn} is deleted.')
    mdata['msg']=data
    return json_data( res,meta=mdata)
