class Pessoa:
    def __init__(self,nome,idade,altura,):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    # método string
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {len(self)}\nAltura: {float(self)}'

    # método lenght
    def __len__(self):
        return self.idade

    # método float
    def __float__(self):
        return self.altura

    # método destrutor
    def __del__(self):
        print(f'Objeto {self.nome} destuído com sucesso!')