class authorize:
    async def password_check(self, code) -> bool:
        truecode = "12452"
        if code == truecode:
            return True
        else:
            print("jopa")
    