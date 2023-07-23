from fastapi import APIRouter
from app.dependencies import SMSProvider

router = APIRouter()

@router.get( "" )
async def accept_sms( login: str, psw: str, phones: str, mes: str, fmt: int, sms_provider: SMSProvider ):
    """ endpoint with smsc.ru contract"""
    list_phones = phones.split(',')

    success = True
    for phone in list_phones:
        success = success and await sms_provider.send( phone=phone, message=mes )

    if success:
        return {
            "id": 1,
            "cnt": 1
        }
    else:
        return {
            "error": "fail",
            "error_code": 8
        }