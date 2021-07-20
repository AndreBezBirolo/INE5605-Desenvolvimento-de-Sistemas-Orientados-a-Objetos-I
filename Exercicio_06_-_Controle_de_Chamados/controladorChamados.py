from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        super().__init__()
        self.__chamados = []
        self.__tiposChamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        c = 0
        if isinstance(tipo, TipoChamado) and tipo is not None:
            for chamado in self.__chamados:
                if chamado.tipo == tipo:
                    c += 1
        return c

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado) -> Chamado:
        if isinstance(data, Date) and data is not None and \
            isinstance(cliente, Cliente) and cliente is not None \
            and isinstance(tecnico, Tecnico) and tecnico is not None \
            and isinstance(titulo, str) and titulo is not None \
            and isinstance(descricao, str) and descricao is not None \
            and isinstance(tipo, TipoChamado) and TipoChamado is not None:
            cAux = 0
            for chamado in self.__chamados:
                if chamado.data == data and chamado.cliente == cliente \
                    and chamado.tecnico == tecnico \
                    and chamado.tipo == tipo:
                    cAux += 1
            if cAux == 0:
                self.__chamados\
                    .append(Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo))
            return self.__chamados[-1]

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) \
        -> TipoChamado:
        if isinstance(codigo, int) and codigo is not None \
            and isinstance(nome, str) and nome is not None \
            and isinstance(descricao, str) and descricao is not None:
            cAux = 0
            for tipo in self.__tiposChamados:
                if tipo.codigo == codigo:
                    cAux += 1
            if cAux == 0:
                self.__tiposChamados \
                    .append(TipoChamado(codigo, descricao, nome))
            return self.__tiposChamados[-1]

    def tipos_chamados(self):
        return self.__tiposChamados
