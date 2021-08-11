class ComandoInvalidoException(Exception):
    def __init__(self):
        super(ComandoInvalidoException, self).__init__("Comando inválido, tente novamente!")
