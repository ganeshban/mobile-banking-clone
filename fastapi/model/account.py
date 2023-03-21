from pydantic import BaseModel


class Account(BaseModel):
    AccountID:str=''
    AccountNumber:str=''
    AccountName:str=''
    DateOpen:str=''
    user:int=0


    def from_list(l:list):
        return Account(l[0],l[1],l[2],l[3],l[4])
    