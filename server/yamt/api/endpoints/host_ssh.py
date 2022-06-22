from uuid import UUID

from fastapi import APIRouter

from yamt.hosts import get_host_storage

host_ssh_credentials_router = APIRouter()
