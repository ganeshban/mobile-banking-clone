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
    result=table.get_all('',f"Select * from tblmembers {data} ")
    if type(result) is list:
        return json_data(member.from_list(result))
    return json_data(result,error=1)


@r.get('/{memsn}')
def get_member(
memsn:int=Path(default=None, title='Member Serial Number',description='Enter a members serial number to get members infomartion',gt=0),
):
    
    mem = table.get_one(memsn)
    if type(mem) is list:
        return json_data(member.from_list(mem))
    return json_data(mem,error=1)


@r.post('/new')
def create_member(newmem:member):
    a=table.save_to_database(newmem.dict())
    return json_data(a)


@r.post('/update/{memsn}')
def update_member(memsn:int,newmem:member):
    updated_mem=table.update_to_database(newmem.dict(), memsn)
    if updated_mem:
        return json_data({'msg':'Update failed ','details':updated_mem}, error=1)
    return json_data('Record Updated succesfully')


@r.delete('/delete/{memsn}')
def delete_member(memsn:int):
    mem=table.delete_from_database(memsn)
    data=''
    if mem:
        data=mem
    else:
        data=f'Member having id {memsn} is deleted.'
    return json_data( data)

