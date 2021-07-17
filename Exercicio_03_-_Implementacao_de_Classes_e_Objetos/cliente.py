class Cliente:
    """Insira aqui o construtor"""

    def __init__(self, nome: str, fone: int, email: str):
        self.__nome = nome
        self.__fone = fone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    """Insira aqui os demais metodos ... """

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def fone(self) -> int:
        return self.__fone

    @fone.setter
    def fone(self, fone: int):
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
class Cliente:
    """Insira aqui o construtor"""

    def __init__(self, nome: str, fone: int, email: str):
        self.__nome = nome
        self.__fone = fone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    """Insira aqui os demais metodos ... """

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def fone(self) -> int:
        return self.__fone

    @fone.setter
    def fone(self, fone: int):
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
