from fastapi.exceptions import HTTPException

from  .database import run_query


def not_found_error(msg='Record not found',code=404, meta={}):
    return json_data(msg, code=code,meta=meta)

def json_data(obj, success=True, error=None, msg='', title='',code=000, rec_cnt=0, access_token='', meta:dict={}):
    ret={}
    _is_success=success
    _title=None
    _msg=None
    _code=None
    _rec_count=0
    _access_token=''


    _meta_error=meta.get('error')
    _meta_title=meta.get('title')
    _meta_msg=meta.get('msg')
    _meta_code=meta.get('code')
    _meta_rec_cnt=meta.get('rec_cnt')
    _meta_access_token=meta.get('token')

    if title:
        _title=title
    else: 
        if _meta_title:
            _title=_meta_title

    if msg:
        _msg=msg
    else: 
        if _meta_msg:
            _msg=_meta_msg

    if code:
        _code=code
    else: 
        if _meta_code:
            _code=_meta_code

    if rec_cnt:
        _rec_count=rec_cnt
    else: 
        if _meta_rec_cnt:
            _rec_count=_meta_rec_cnt

    if access_token:
        _access_token=access_token
    else: 
        if _meta_access_token:
            _access_token=_meta_access_token

    

    if _meta_error or error:
        _is_success=False


    if _is_success:
        ret['status']='success'
        ret['record_count']=_rec_count
    else:
        ret['status']='failed'
        ret['record_count']=-1
    ret['title']=_title
    ret['message']=_msg
    ret['code']=_code
    ret['access_token']=_access_token
    ret['data']=obj

    
    _my_code=200
    if _code:
        _my_code=_code
    raise HTTPException(_my_code,ret)


class DB_Table():
    def __init__(self,tableName,uniquefield='sn',module_name=None) -> None:
        self.table_name=tableName
        self.unique_filed=uniquefield
        self.module_name=module_name

    
    def get_all(self,condition,qry=None):
        data=None
        if qry:
            data = run_query(qry)
        data = run_query(f'select * from {self.table_name } {condition}')
        return return_with_meta(data,f'record not found')

    def get_one(self, id):
        data=run_query(f'select * from {self.table_name} where {self.unique_filed} = {id}')
        return return_with_meta(data,f'record not found with {id}')


    def delete_from_database(self,id):
        data=run_query(f'delete from {self.table_name} where {self.unique_filed} = {id}')
        return return_with_meta(data,'Record not deleted. Deletion faild.','d')



    def save_to_database(self,entity:dict):
        values=''
        for key,val in entity.items():
            if type(val) is str :
                values+=f"'{val}', "
            else:  
                values+=f'{val}, '
        values=values.removesuffix(', ')
        fullSQL=f'Insert into {self.table_name} values ( {values} ) '
        return return_with_meta(run_query(fullSQL),'failed to save data to database','c')


    def update_to_database(self,data:dict, uniqueVal=None):
        values=''
        unique_val=uniqueVal
        for key,val in data.items():

            if not unique_val:
                if key==self.unique_filed:
                    unique_val=val
            
            if type(val) is str :
                values+=f" {key} = '{val}', "
            else:  
                values+=f' {key} = {val}, '
        values=values.removesuffix(', ')
        fullSQL=f'Update {self.table_name} set {values} where {self.unique_filed} = {unique_val} '
        return return_with_meta(run_query(fullSQL),'error occered while updation','u')


    def custom_query(self, query:str):
        return return_with_meta(run_query(query),'something went wrong check your Query again.','n')


def return_with_meta(source,errorMsg='',CRUD='r'):
    data,row=source
    if type(data)==str or (len(data)==0 and row==0):
        meta={'rec_cnt':-1,'msg':errorMsg,'title':'error','error':1}
    else:
        meta={'rec_cnt':len(data)}
    if CRUD=='c':
        if row>0:
            meta['code']=201
        else:
            meta['code']=200
    elif CRUD=='r':
        if len(data)>0:
            meta['code']=200
        else:
            meta['code']=404
    elif CRUD=='u':
        if row>0:
            meta['code']=200
        else:
            meta['code']=404
    elif CRUD=='d':
        if row>0:
            meta['code']=410
        else:
            meta['code']=404
    else:
        meta['code']=201
    return data, meta
