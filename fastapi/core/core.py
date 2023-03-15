
def json_data(obj, error=None, success=None, errorMsg='', successMsg='',code=1):
    ret={}
    ret['Success']=True
    ret['sMessage']=successMsg
    ret['Error']=False
    ret['eMessage']=errorMsg

    ret['Code']=code
    ret['data']=obj

    if error:
        ret['Error']=True
        ret['Success']=False
    if success:
        ret['Error']=False
        ret['Success']=True
    return ret


class DB:
    def __init__(self,_DB_Name:str='') -> None:
        self.db_name=_DB_Name
class DB_Table(DB):
    def __init__(self,_tableName:str=''):
        super().__init__()
        self.table_name=_tableName
    def save_to_database(self):
        return self.table_name
class DB_Views(DB):
    def __init__(self,_viewName:str='') -> None:
        super().__init__()
class DB_Function(DB):
    def __init__(self,_functionName:str='') -> None:
        super().__init__()
class DB_Procider(DB):
    def __init__(self,_prociderName:str='') -> None:
        super().__init__()

