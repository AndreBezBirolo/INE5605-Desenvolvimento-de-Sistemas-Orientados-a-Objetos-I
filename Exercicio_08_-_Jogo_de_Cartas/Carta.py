from AbstractCarta import *

from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        if isinstance(personagem, Personagem) and personagem is not None:
            self.__personagem = personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''

    def valor_total_carta(self) -> int:
        return self.__personagem.energia + \
               self.__personagem.resistencia + \
               self.__personagem.velocidade + \
               self.__personagem.habilidade

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
