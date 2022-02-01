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
