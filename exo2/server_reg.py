from pydantic import BaseModel


class ServerReg(BaseModel):
    name: str
    adress : str
