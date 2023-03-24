from pydantic import BaseModel


class Users(BaseModel):
    userid:str=''
    username:str
    userpassword:str
    email:str=''
    phone:str=''
    fullname:str=''
    isactive:int=1

    def from_list(lst:str):
        if len(lst)==1:
            l=lst[0]
            return Users(userid=l[0],username=l[1],userpassword=l[2],email=l[3],phone=l[4],fullname=l[5],isactive=l[6])
        else:
            list=[]
            for i in lst:
                l=i
                data=Users(userid=l[0],username=l[1],userpassword=l[2],email=l[3],phone=l[4],fullname=l[5],isactive=l[6])
                list.append(data)
            return list
