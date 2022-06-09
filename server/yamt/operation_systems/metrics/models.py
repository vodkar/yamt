from pydantic import BaseModel


class OSVersion(BaseModel):
    name: str | None
    version: str | None
    os_id: str | None
    os_like_id: str | None
    core_version: str | None
