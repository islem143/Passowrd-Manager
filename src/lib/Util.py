from ..globals import GLOBAL


class Util:

    @staticmethod
    def is_password_valid(string: str, tocompare: str, method) -> bool:
        return method(string, tocompare)

    @staticmethod
    def set_global(key: str, value: any) -> None:

        GLOBAL[key] = value

    @staticmethod
    def is_connected() -> bool:
        return GLOBAL["key"] != None
