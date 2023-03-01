from authorization import authorize


class MainService:
    @staticmethod
    async def password_check(
        code: str
        )-> bool:
        await authorize.password_check(code)