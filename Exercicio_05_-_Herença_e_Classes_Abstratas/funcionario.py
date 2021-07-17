from abc import abstractmethod
from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU):

    @abstractmethod
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        if isinstance(departamento, str):
            self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return f'do departamento "{self.__departamento}"' + super().emprestar(titulo_livro)

    @abstractmethod
    def devolver(self, titulo_livro: str):
        return f'do departamento "{self.__departamento}"' + super().devolver(titulo_livro)
