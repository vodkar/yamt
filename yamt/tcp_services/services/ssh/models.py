from pydantic import BaseModel


class SSHPasswordAuthentication(BaseModel):
    user: str
    password: str
