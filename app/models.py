from sqlalchemy import Column, Integer, String, DateTime, func # type: ignore
from database import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    message = Column(String(500))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
