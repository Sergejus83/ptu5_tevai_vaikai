from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker




engine = create_engine('sqlite:///data/tevai_vaikai.db')
# Base klese paveldes i domenu base
Base = declarative_base()

class Tevas(Base):
    __tablename__  = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavardė", String)

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde})"


class Vaikas(Base):
    __tablename__  = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavardė", String)
    mokymo_istaiga = Column("mokykla",  String, nullable=True)
    # Foreigen key veda i i lenteles pavadinima
    tevas_id = Column("tevas_id", Integer, ForeignKey("tevas.id")) # - domenu bazes
    # Foreigen key veda i Objekto pavadinima
    tevas = relationship("Tevas") # - python'o

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.tevas})"


if __name__=="__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

















# class Tevas(Base):
#     __tablename__ = "tevas"
#     id = Column(Integer, primary_key=True)
#     vardas = Column("Vardas", String)
#     pavarde = Column("Pavardė", String)
#     vaikas_id = Column(Integer, ForeignKey('vaikas.id'))
#     vaikas = relationship("Vaikas")


# class Vaikas(Base):
#     __tablename__ = "vaikas"
#     id = Column(Integer, primary_key=True)
#     vardas = Column("Vardas", String)
#     pavarde = Column("Pavardė", String)
#     mokymo_istaiga = Column("Mokymo įskaita", String)



# Base.metadata.create_all(engine)
