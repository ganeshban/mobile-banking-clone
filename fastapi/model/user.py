from core.core import DB_Table
from pydantic import BaseModel


class Users(BaseModel):
    userid:str=''
    username:str
    userpassword:str
    email:str=''
    phone:str=''
    fullname:str=''
    isactive:str=''

class User(DB_Table, Users):
    __tblname='tblusers'

    def __init__(self,userID, username, userpassword, email, phone,fullname,isactive):
        super().__init__(self.__tblname)
        self.userid=userID
        self.username=username
        self.userpassword=userpassword
        self.email=email
        self.phone=phone
        self.fullname=fullname
        self.isactive=isactive
        

    def from_DB(self, *args):
        '''Pass the Condition as an argument
        
        '''
        return 'this function will return users from data base'

    def Save_to_database(self):
        if self.__tblname:
            print('this will have db objects')
    
        return 'this function will return users from data base'


