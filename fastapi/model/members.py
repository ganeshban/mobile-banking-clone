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
    active:int=1

    def from_list(lst:str):
        if len(lst)==1:
            l=lst[0]
            return Members(sn=l[0],memid=l[1],fname=l[2],mname=l[3],lname=l[4],dob=l[5],doa=l[6],address=l[7],active=l[8])
        else:
            list=[]
            for i in lst:
                l=i
                data=Members(sn=l[0],memid=l[1],fname=l[2],mname=l[3],lname=l[4],dob=l[5],doa=l[6],address=l[7],active=l[8])
                list.append(data)
            return list
            
    def to_dict(lst:str):
        if len(lst)==1:
            l=lst[0]
            acc= Members(sn=l[0],memid=l[1],fname=l[2],mname=l[3],lname=l[4],dob=l[5],doa=l[6],address=l[7],active=l[8])
            return acc.dict()
        else:
            list=[]
            for i in lst:
                l=i
                data=Members(sn=l[0],memid=l[1],fname=l[2],mname=l[3],lname=l[4],dob=l[5],doa=l[6],address=l[7],active=l[8])
                accs=data.dict()
                list.append(accs)
            return list
