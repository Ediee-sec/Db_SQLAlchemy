from time import strftime, localtime
from datetime import datetime

class insere_produto():
    def __init__(self):
        self.produto = int(input('Qual o código: '))
        self.descricao = str(input('Descrição do produto: '))

    def codigo_produto(self):
        return rRet.produto
    def descri_produto(self):
        return rRet.descricao

rRet = insere_produto()

class insere_funcionario():
    def __init__(self):
        self.nome = str(input('Nome do Funcionário: '))
        self.sobrenome = str(input('Sobrenome do Funcionário: '))
        self.datanasc = datetime.strptime(input("Data de Nascimento: "), '%d/%m/%Y')

    def nome_funcionario(self):
        return lRet.nome
    def sobrenome_funcionario(self):
        return lRet.sobrenome
    def data_funcionario(self):
        return lRet.datanasc
    def idade_funcionario(self):
        var_funcionario = datetime.today() - lRet.datanasc()
        return var_funcionario
lRet = insere_funcionario()