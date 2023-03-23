from pydantic import BaseModel


class AskRequest(BaseModel):
    id: str
    text: str
