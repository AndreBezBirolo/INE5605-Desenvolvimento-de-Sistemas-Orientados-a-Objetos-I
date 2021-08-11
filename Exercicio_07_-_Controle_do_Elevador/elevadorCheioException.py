class ElevadorCheioException(Exception):
    def __init__(self):
        super(ElevadorCheioException, self).__init__("O elevador está cheio!")
