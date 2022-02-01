from main import  produtos
from entrada import insere_produto

def insert():
    produto = produtos(codProd = insere_produto.codigo_produto(True),
                       desProd = insere_produto.descri_produto(True))
    print(produto)

if __name__ == '__main__':
    insert()

