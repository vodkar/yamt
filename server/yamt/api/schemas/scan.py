from uuid import UUID

from pydantic import BaseModel, IPvAnyAddress, IPvAnyNetwork


class PostNetworksSchema(BaseModel):
    networks: list[IPvAnyNetwork]
    
class ShortNetworkRelatedHost(BaseModel):
    id: UUID
    ip: IPvAnyAddress
