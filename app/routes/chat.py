from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession # type: ignore
from ..websocket_manager import ConnectionManager
from ..database import get_db
from ..models import ChatMessage

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str, db: AsyncSession = Depends(get_db)):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            # Save to DB
            new_msg = ChatMessage(username=username, message=data)
            db.add(new_msg)
            await db.commit()
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(username)
