from fastapi import WebSocket
class SMSProvider:
    def __init__(self) -> None:
        self.connections: dict[str,WebSocket] = {}

    async def register( self, websocket: WebSocket, phone: str ):
        await websocket.accept()
        self.connections[phone] = websocket

    async def send( self, phone: str, message: str ):
        if phone in self.connections:
            await self.connections[phone].send_text( message )