from cliente import Cliente
from pacote_viagem import PacoteViagem


class Venda:
    """Insira aqui todos metodos e atributos ... """

    def __init__(self, codigo: int, cliente: Cliente, descricao: str,
                 pacote: PacoteViagem, quantidade: int):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__descricao = descricao
        self.__pacote = pacote
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pacote(self) -> PacoteViagem:
        return self.__pacote

    @pacote.setter
    def pacote(self, pacote: PacoteViagem):
        if isinstance(pacote, PacoteViagem):
            self.__pacote = pacote

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def preco_total(self):
        return self.__quantidade * self.__pacote.custo_unitario
