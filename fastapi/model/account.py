from pydantic import BaseModel
from .user import Users

class Account(BaseModel):
    AccountID:str
    AccountNumber:str
    AccountName:str
    DateOpen:str
    user:Users
