class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        super().__init__("O elevador já se encontra no último andar!")
