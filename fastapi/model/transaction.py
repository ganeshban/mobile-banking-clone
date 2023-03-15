from pydantic import BaseModel
from .user import Users
from .account import Account

class Transaction(BaseModel):
    tid:str
    Date:str
    user:Users
    accountID:Account
    DrAmt:float
    CrAmt:float
    remarks:str



users=Users(UserID='ganeshban', phone='7207519966',username='ganeshban',userpassword='pasw',email='banganesh98@gmail.com',fullname='ganesh ban',isactive=1)


