from fastapi_utils.api_model import APIModel
from pydantic import BaseModel


class UserUciBase(APIModel):
    username: str
    pass


class UserUciIn(UserUciBase):
    password: str
    pass


class UserUciOut(UserUciBase):
    email: str
    display_name: str
    title: str
