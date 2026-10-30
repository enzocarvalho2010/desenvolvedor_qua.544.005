class Pessoa:
    def __init__(self,nome,idade,email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def cumprimentar(self):
        print(f'Olá, sou {self.nome}, tenho {self.idade} anos e meu email é {self.email}.')