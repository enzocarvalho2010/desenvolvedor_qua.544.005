# classe
class Pessoa:
    # construtor
    def __init__(self,nome,idade,email,cpf):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf
    
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Email: {self.email}')
        print(f'CPF: {self.cpf}')

def main():
    # instanciar classe
    user = Pessoa(nome='',idade=0,email='',cpf='')

    #insere valores nos atributos
    user.nome = input('Informe o nome: ').strip().title()
    user.idade = int(input('Informe a idade: '))
    user.email = input('Informe o email: ').strip().lower()
    user.cpf = input('Informe o CPF: ').strip()

    #exibe atributos na tela
    print(f'Nome: {user.nome}')
    print(f'Idade: {user.idade}')
    print(f'Email: {user.email}')
    print(f'CPF: {user.cpf}')

    user.exibir_dados()

if __name__ == '__main__':
    main()