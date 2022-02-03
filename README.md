## Sistema de cadastramento

* #### *Contexto da aplicação:*

*Após dias estudando sobre o SQLAlchemy para aplicar um banco de dados para uma API que estou desenvolvendo, resolvi por parte deste conhecimento em prática, com este Db simples, aproveiei para testar também meus conhecimentos em modularixzação no Python e POO*

* #### *Mapa do código:*

1. **Modulo main, responsável por criar a instancia com o SQLite e desenvolver o Db**

```Python
from sqlalchemy import  create_engine, Column, Integer, String, DATETIME
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Mercadinho.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

base = declarative_base()
base.query = db_session.query_property()

class produtos(base):
    __tablename__='produtos'
    id = Column(Integer, primary_key=True)
    codProd = Column(String(9), index=True)
    desProd = Column(String(30))

    def comita(self):
        db_session.add(self)
        db_session.commit()

    def __repr__(self):
        return f'Descrição do produto: {self.desProd}\nCódigo do Produto: {self.codProd}'

class funcionarios(base):
    __tablename__= 'funcionarios'
    id = Column(Integer, primary_key=True)
    nomeFun = Column(String(10))
    sobrFun = Column(String(15))
    dataNas = Column(DATETIME())

    def __repr__(self):
        return f'Nome {self.nomeFun}'

def init_db():
    base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
```

****

2. **Modulo entrada, responsável por criar as classes e métodos que irão retornar os valores digitados pelo usuário na interface**

```Python
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
```
****

3. **Modulo query, responsável por realizar as devidas consultas,inserção,atualização ou exclusão do banco de dados**
*Para este exemplo coloquei apenas o método de inserção*

```Python
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





```