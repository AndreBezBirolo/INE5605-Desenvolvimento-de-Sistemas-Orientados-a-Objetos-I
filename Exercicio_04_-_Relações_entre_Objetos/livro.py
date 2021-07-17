from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora,
                 autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(ano, int):
            self.__ano = ano
        if isinstance(editora, Editora) and editora is not None:
            self.__editora = editora
        if isinstance(autor, Autor) and autor is not None:
            self.__autores = [autor]
        if isinstance(numero_capitulo, int) \
            and isinstance(titulo_capitulo, str) \
            and numero_capitulo is not None \
            and titulo_capitulo is not None:
            self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]


    @property
    def codigo(self) -> int:
        return self.__codigo


    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo


    @property
    def titulo(self):
        return self.__titulo


    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


    @property
    def ano(self):
        return self.__ano


    @ano.setter
    def ano(self, ano):
        self.__ano = ano


    @property
    def editora(self):
        return self.__editora


    @editora.setter
    def editora(self, editora):
        self.__editora = editora


    @property
    def autores(self):
        return self.__autores


    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor is not None and autor not in self.__autores:
            self.__autores.append(autor)


    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor is not None and autor in self.__autores:
            self.__autores.remove(autor)


    def incluir_capitulo(self, numero: int, titulo: str):
        if isinstance(numero, int) and numero is not None and isinstance(titulo, str) and titulo is not None:
            count_include = 0
            fix_list = 0
            while fix_list < len(self.__capitulos):
                if titulo == self.__capitulos[fix_list].titulo:
                    count_include += 1
                fix_list += 1
            if count_include == 0:
                self.__capitulos.append(Capitulo(numero, titulo))


    def excluir_capitulo(self, titulo: str):
        if isinstance(titulo, str) and titulo is not None:
            count_exclude = 0
            while self.__capitulos:
                if titulo == self.__capitulos[count_exclude].titulo:
                    self.__capitulos.pop(count_exclude)
                    break
                count_exclude += 1


    def find_capitulo_by_titulo(self, titulo: str):
        if isinstance(titulo, str) and titulo is not None:
            count_find = 0
            while count_find < len(self.__capitulos):
                if titulo in self.__capitulos[count_find].titulo:
                    return self.__capitulos[count_find]
                count_find += 1
