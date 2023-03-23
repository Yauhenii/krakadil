from pydantic import BaseModel


class DumpRequest(BaseModel):
    text: str
