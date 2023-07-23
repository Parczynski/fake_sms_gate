from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from app.dependencies import SMSProvider
from app.routes import smsc

app = FastAPI()


@app.websocket( "/ws" )
async def otp_ws( websocket: WebSocket, phone: str, sms_provider: SMSProvider ):
    await sms_provider.register( websocket=websocket, phone=phone )
    while True:
        data = await websocket.receive_text()
    
app.include_router( smsc.router, prefix="/smsc" )

app.mount( "/", StaticFiles(directory="dist", html=True), name="static")