from pydantic import BaseModel


class AskResponse(BaseModel):
    id: str
    text: str
