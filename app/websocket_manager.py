from fastapi import WebSocket # type: ignore
from typing import Dict

class ConnectionManager():
    def __init__(self):
        self.active_connections : dict[str , WebSocket] = {}

    async def connect(self , websocket : WebSocket , username : str) :
        await websocket.accept()
        self.active_connections[username]  = websocket
        await self.broadcast(f"{username} joined the chat!!")

    async def disconnect(self , username : str):
        self.active_connections.pop[username , None]
        await self.boardcast(f"{username} left the chat!!")

    async def broadcast(self , message :str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

