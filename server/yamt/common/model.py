from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class YamtModel(BaseModel):
    pass

class YamtModelWithId(YamtModel):
    id: UUID = Field(default_factory=uuid4)
