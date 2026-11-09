class Departamento:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

class Empresa:
    def __init__(self,razao,fantasia,cnpj,departamento):
        self.__razao = razao
        self.__fantasia = fantasia
        self.__cnpj = cnpj
        self.__departamento = departamento

    @property
    def razao(self):
        return self.__razao
    @razao.setter
    def razao(self,razao):
        self.__razao = razao

    @property
    def fantasia(self):
        return self.__fantasia
    @fantasia.setter
    def fantasia(self,fantasia):
        self.__fantasia = fantasia

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,cnpj):
        self.__cnpj = cnpj

    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self,departamento):
        self.__departamento= departamento

    def detalhes(self):
        return f'Razão Social: {self.__razao}\nNome da Empresa: {self.__fantasia}\nCNPJ: {self.__cnpj}\nDepartamento: {self.__departamento.nome}'