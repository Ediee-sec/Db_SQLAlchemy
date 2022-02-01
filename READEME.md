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

    def __repr__(self):
        return f'Descrição do produto: {self.desProd}\nCódigo do Produto: {self.codProd}'

class funcionarios(base):
    __tablename__= 'funcionarios'
    id = Column(Integer, primary_key=True)
    nomeFun = Column(String(10), index=True)
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
```
****

3. **Modulo query, responsável por realizar as devidas consultas,inserção,atualização ou exclusão do banco de dados**
*Para este exemplo coloquei apenas o método de inserção*

```Python
from main import  produtos
from entrada import insere_produto

def insert():
    produto = produtos(codProd = insere_produto.codigo_produto(True),
                       desProd = insere_produto.descri_produto(True))
    print(produto)

if __name__ == '__main__':
    insert()


```