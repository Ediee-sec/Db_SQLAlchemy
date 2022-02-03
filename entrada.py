class insere_produto():
    def __init__(self):
        self.produto = ''
        self.descricao = ''

    def codigo_produto(self):
        self.produto = input('Qual o código: ')
        resultado = self.produto
        return resultado
    def descri_produto(self):
        self.descricao = input('Qual a Descricao: ')
        resultado = self.descricao
        return resultado

rRet = insere_produto()

class query():
    def __init__(self):
        self.cod = ''

    def codigo(self):
        self.cod = (input('Informe o codigo da Consulta: '))
        resultado = self.cod
        return resultado
qQuery = query()





