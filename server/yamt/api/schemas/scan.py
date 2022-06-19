
from pydantic import BaseModel, IPvAnyNetwork


class NetworksSchema(BaseModel):
    networks: list[IPvAnyNetwork]
