from fastapi import WebSocket


class SMSProvider:
    def __init__(self) -> None:
        self.connections: dict[str,WebSocket] = {}
        self.registrations = 0
        self.messages = 0

    async def register( self, websocket: WebSocket, phone: str ):
        await websocket.accept()
        self.connections[phone] = websocket
        self.registrations+=1
        await websocket.send_json( { "id": f'{self.registrations}_registration', "content":f'{phone} зарегистрирован' })

    async def send( self, phone: str, message: str ):

        
        if phone in self.connections:
            self.messages += 1
            await self.connections[phone].send_json( { "id": f'{self.messages}_message', "content": message })
            return True
        
        return False