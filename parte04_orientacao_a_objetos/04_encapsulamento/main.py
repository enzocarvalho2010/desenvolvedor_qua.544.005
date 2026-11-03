from model import Pessoa

def main():
    user = Pessoa(nome='',idade=0,cpf='',telefone='',email='')
    user.nome =  input('Insira o nome: ').strip().title()
    user.idade =  int(input('Insira a idade: ').strip())
    user.cpf =  input('Insira o CPF: ').strip()
    user.telefone =  input('Insira o telefone: ').strip()
    user.email =  input('Insira o email: ').strip().lower()

    print(f'Nome: {user.nome}')
    print(f'Idade: {user.idade} anos')
    print(f'CPF: {user.cpf}')
    print(f'Telefone: {user.telefone}')
    print(f'Email: {user.email}')
    
if __name__ == '__main__':
    main()