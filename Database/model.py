from sqlalchemy import Column,Integer,String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session,sessionmaker


Base=declarative_base()


class Smartphone(Base):

    __tablename__='smartphones'

    id=Column(Integer,autoincrement=True,primary_key=True)
    brand=Column(String)
    rom=Column(String)
    ram=Column(String)
    Camera=Column(String)

if __name__=="__main__":

       engine=create_engine("sqlite:///mydatabase.sqlite")


       #connect to your database
       Base.metadata.create_all(engine)
       Session = sessionmaker(bind=engine)
       session=Session()



