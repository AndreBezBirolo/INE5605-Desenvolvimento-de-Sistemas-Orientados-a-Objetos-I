class ElevadorJahVazioException(Exception):
    def __init__(self):
        super(ElevadorJahVazioException, self).__init__("O elevador já se encontra vazio.")
