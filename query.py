from main import  produtos
from entrada import rRet, qQuery

def insere_produtos():
    produto = produtos(codProd = rRet.codigo_produto(),
                       desProd = rRet.descri_produto())
    produto.comita()


def consulta():
    cQuery = produtos.query.filter_by(codProd = qQuery.codigo()).first()
    print(cQuery)

if __name__ == '__main__':
    opc = input('Informe oque deseja fazer no Db\nInserir = 1\nconsultar = 2\n')
    if opc == '1':
        insere_produtos()
    elif opc == '2':
        consulta()


