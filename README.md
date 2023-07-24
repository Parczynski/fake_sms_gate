# Fake SMS Gateway

Full stack service for testing one time passwords. The intension of this service is to use it in development/sandbox environments of your system instead of actual SMS provider endpoint. So that you can test any flows requiring sending SMS without using third-party SMS provider and sending real SMS.

## How to run

You will need python 3+ and Node.js 16+ installed on your local machine.

```sh
# clone repository
git clone git@github.com:Parczynski/fake_sms_gate.git
cd fake_sms_gate

# install python dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# install nodejs dependencies and build frontend
npm ci
npm run build

# run the service
python -m app.main
```


## How to use

First of all you need to open the service in browser which is available on port 3000 by default. Fill the form with any phone number you want to use for testing and click "Set Number" button. You will see the message that this number is registered.

Next you can use sms endpoint to fake sending sms and show SMS text in your browser. By default this service has only one endpoint with route */smsc*. This endpoint follows contracts of this sms provider https://smsc.ru/api/#menu. 

To test the service at this step you can send following GET request: *http://localhost:3000/smsc?login=123&psw=123&phones=[phone]&fmt=3&mes=test*, where **[phone]** should be replaced with urlencoded phone number you have specified in previouse step. Text under **mes** parameter should appear on the frontend.

You can also register different phone numbers on separate tabs/browsers/devices and messages will be delivered to the appropriate target.

To make this service possible to replace your actual SMS provider can either change existing */smsc* route handler in file *app/routes/smsc.py* or you could copy this file to create new endpoint corresponding to your provider's API schema and include a new router in *app/server.py*.

```python
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from app.dependencies import SMSProvider
from app.routes import smsc
from app.routes import your_endpoint # import your file here

app = FastAPI()


@app.websocket( "/ws" )
async def otp_ws( websocket: WebSocket, phone: str, sms_provider: SMSProvider ):
    await sms_provider.register( websocket=websocket, phone=phone )
    while True:
        data = await websocket.receive_text()
    
app.include_router( smsc.router, prefix="/smsc" )
app.include_router( your_endpoint.router, prefix="/your_endpoint" ) # include your router here

app.mount( "/", StaticFiles(directory="dist", html=True), name="static")
```