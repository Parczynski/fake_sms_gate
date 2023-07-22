from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from .sms_provider import SMSProvider

app = FastAPI()
sms_provider = SMSProvider()


@app.websocket( "/ws" )
async def otp_ws( websocket: WebSocket, phone: str ):
    await sms_provider.register( websocket=websocket, phone=phone )
    while True:
        data = await websocket.receive_text()
    
@app.get( "/send" )
async def accept_sms( login: str, psw: str, phones: str, mes: str, fmt: int ):
    """ endpoint with smsc.ru contract"""
    list_phones = phones.split(',')
    for phone in list_phones:
        await sms_provider.send( phone=phone, message=mes )

    return {
        "id": 1,
        "cnt": 1
    }

app.mount( "/", StaticFiles(directory="dist", html=True), name="static")