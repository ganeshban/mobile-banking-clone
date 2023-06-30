from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from model.user import Users
from core.core import json_data, DB_Table


table = DB_Table('tblusers', 'userid')
r = APIRouter(tags=['User'])

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7fgjasdgfjajdshjfagdfja"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
metadata = None


@r.get('/login')
async def login(
    username: str = Query(default='', title='User Name',
                          description='Enter a User Name for login', min_length=5),
    password: str = Query(default='', title='Password',
                          description='Enter a Password for login', min_length=5)
):
    user = get_user_from_database(username, password)
    if not user:
        return not_found_error()

    token = await get_token(user)
    return json_data(user.__dict__, meta=metadata, access_token=token.get("access_token"))


def get_user_from_database(username: str | None, password: str | None):
    global metadata
    where = ''
    if username:
        where = f" where username = '{username}' "
    if password:
        where += f"and userpassword = '{password}' "
    result, _ = table.get_all(where)
    metadata = _
    if not result:
        not_found_error()
    return Users.from_list(result)


def not_found_error():
    return json_data("either username or password is wrong.", code=404, meta=metadata)


def get_password_hash(password):
    return pwd_context.hash(password)


def encode_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def decode_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    return username


async def get_token(user: Users):
    access_token = encode_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@r.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_from_database(form_data.username, form_data.password)
    if not user:
        not_found_error()
    token = await get_token(user)
    return json_data(user.__dict__, meta=metadata, access_token=token.get("access_token"))
