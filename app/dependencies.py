from app.sms_provider import SMSProvider as SMSProviderClass
from functools import lru_cache
from typing import Annotated
from fastapi import Depends


@lru_cache
def get_sms_provider():
    return SMSProviderClass()



SMSProvider = Annotated[ SMSProviderClass, Depends(get_sms_provider) ]

