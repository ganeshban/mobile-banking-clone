from pydantic import BaseModel



class Members(BaseModel):
    
    sn:int
    memid:int
    fname:str=''
    mname:str=''
    lname:str=''
    dob:str=''
    doa:str=''
    address:str=''
    active:bool=True

MembersList=[]
