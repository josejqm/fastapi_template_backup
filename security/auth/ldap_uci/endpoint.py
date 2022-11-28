from typing import Any

from fastapi import APIRouter

from .ldap_uci import ldap_uci
from .schemas import *

router = APIRouter(
    prefix="/auth/uci",
    tags=["auth"],
)


@router.post("/login", response_model=UserUciOut | None)
async def authenticate(user: UserUciIn) -> Any:
    return ldap_uci.authenticate(user.username, user.password)
