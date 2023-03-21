from  database.dbhelper import run_query

def json_data(obj, success=True, error=None, msg='', title='',code=1, meta:dict=None):
    ret={}

    _meta_error=meta.get('error')
    _meta_success=meta.get('success')
    _meta_title=meta.get('title')
    _meta_msg=meta.get('msg')
    _meta_code=meta.get('code')

    _status=None
    _title=None
    _msg=None
    _code=None



    _is_success=meta['Error']
    _is_success=success

    if error:
        ret['Status']='failed'
        _is_success=False
    if _is_success:
        ret['Status']='success'


    ret['Title']=title
    ret['Message']=msg
    ret['Code']=code
    ret['data']=obj

    return ret


class DB_Table():
    def __init__(self,tableName,uniquefield='sn',module_name=None) -> None:
        self.table_name=tableName
        self.unique_filed=uniquefield
        self.module_name=module_name

    
    def get_all(self,condition,qry):
        if qry:
            return run_query(qry)
        return run_query(f'select * from {self.table_name } {condition}')
        

    def get_one(self, id):
        data=run_query(f'select * from {self.table_name} where {self.unique_filed} = {id}')
        return data


    def delete_from_database(self,id):
        data,row=run_query(f'delete from {self.table_name} where {self.unique_filed} = {id}')
        if row>0:
            return data
        else:
            return 'Record not deleted. Deletion faild.'



    def save_to_database(self,data:dict):
        values=''
        for key,val in data.items():
            if type(val) is str :
                values+=f"'{val}', "
            else:  
                values+=f'{val}, '
        values=values.removesuffix(', ')
        fullSQL=f'Insert into {self.table_name} values ( {values} ) '
        data=run_query(fullSQL)
        return data


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
        data=run_query(fullSQL)
        return data


    def run_query(query:str):
        return run_query(query)
