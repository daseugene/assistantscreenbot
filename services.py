from authorization import authorize
from selenium import webdriver
import time

class MainService:
    @staticmethod
    async def password_check(code)-> bool:
        return await authorize.password_check(code) 

```