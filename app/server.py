from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from app.sms_provider import SMSProvider

app = FastAPI()

sms_provider = SMSProvider()

app.mount( "/", StaticFiles(directory="dist", html=True), name="static")

@app.websocket( "/ws" )
async def sms_gate( ws: WebSocket, phone: str ):
    await sms_provider.register( websocket=ws, phone=phone )
    while True:
        data = await ws.receive_text()