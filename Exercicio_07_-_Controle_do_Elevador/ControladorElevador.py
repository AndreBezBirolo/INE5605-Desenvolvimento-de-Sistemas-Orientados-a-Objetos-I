from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    def subir(self) -> int:
        return Elevador.subir(self.__elevador)

    def descer(self) -> int:
        return Elevador.descer(self.__elevador)

    def entra_pessoa(self) -> int:
        return Elevador.entra_pessoa(self.__elevador)

    def sai_pessoa(self) -> int:
        return Elevador.sai_pessoa(self.__elevador)

    def inicializar_elevador(self, andar_atual: int, total_andares_predio: int,
                             capacidade: int, total_pessoas: int):
        if type(andar_atual) is not int or type(total_andares_predio) \
                is not int or type(capacidade) is not int \
                or type(total_pessoas) is not int:
            raise ComandoInvalidoException
        if andar_atual < 0 or total_andares_predio < 0 \
                or capacidade < 0 or total_pessoas < 0:
            raise ComandoInvalidoException
        elif andar_atual < 0 or total_andares_predio < 0 \
                or total_pessoas > capacidade \
                or andar_atual > total_andares_predio:
            raise ComandoInvalidoException
        else:
            self.__elevador = Elevador(capacidade, total_pessoas,
                                       total_andares_predio, andar_atual)

    @property
    def elevador(self) -> Elevador:
        return self.__elevador
