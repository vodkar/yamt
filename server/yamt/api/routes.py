from fastapi import APIRouter

from .endpoints.hosts import host_router
from .endpoints.scan import scan_router
from .endpoints.topology import topology_router

api_router = APIRouter()
api_router.include_router(scan_router, prefix="/networks", tags=["networks"])
api_router.include_router(host_router, prefix="/hosts", tags=["hosts"])
api_router.include_router(topology_router, prefix="/topology", tags=["topology"])
