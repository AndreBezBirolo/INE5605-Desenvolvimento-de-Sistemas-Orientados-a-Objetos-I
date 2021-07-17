from aluno import Aluno


class AlunoPosGraduacao(Aluno):

    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese):
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese
            if self.__elaborando_tese:
                self.dias_de_emprestimo = self.dias_de_emprestimo * 2

    def emprestar(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        if isinstance(titulo_livro, str):
            return super().devolver(titulo_livro)
