class Cliente:
    def __init__(self, nome, senha):
        if not nome.replace(" ", "").isalpha():
            raise ValueError("O nome só pode conter letras e espaços.")
        if " " in senha:
            raise ValueError("A senha não pode conter espaços.")
        self._nome = nome
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    def validar_senha(self, senha):
        return self._senha == senha
