from pydantic import BaseModel
from datetime import datetime

class ChatMessageCreate(BaseModel):
    username: str
    message: str

class ChatMessageResponse(BaseModel):
    id: int
    username: str
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True
