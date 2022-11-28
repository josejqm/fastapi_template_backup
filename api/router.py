from fastapi import APIRouter

from security.auth.ldap_uci import endpoint as ldap_auth
from api.endpoints import person

app_router = APIRouter()

# Endpoints

# Auth
app_router.include_router(ldap_auth.router)

# Resources
app_router.include_router(person.router)
