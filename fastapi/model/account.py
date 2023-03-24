from pydantic import BaseModel


class Account(BaseModel):
    AccountID:str=''
    AccountNumber:str=''
    AccountName:str=''
    DateOpen:str=''
    userId:int=0


    def from_list(lst:str):
        if len(lst)==1:
            l=lst[0]
            return Account(AccountID=l[0],AccountName=l[1],AccountNumber=l[2],DateOpen=l[3],user=l[4])
        else:
            list=[]
            for i in lst:
                l=i
                data=Account(AccountID=l[0],AccountName=l[1],AccountNumber=l[2],DateOpen=l[3],user=l[4])
                list.append(data)
            return list
