from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/bank_account.db')
Base = declarative_base()


            # Lentele Asmuo
class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key = True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asm_kodas = Column("asm_kodas", Integer)
    tel_numeris = Column("tel_numeris", Integer)
    saskaitos = relationship("Saskaita", back_populates = "asmuo")

    def __init__(self, vardas, pavarde, asm_kodas, tel_numeris): # tada nereikia __init__
        self.vardas=vardas
        self.pavarde=pavarde
        self.asm_kodas=asm_kodas
        self.tel_numeris=tel_numeris
    
    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.asm_kodas}, {self.tel_numeris})"


            # Lentele Bankas
class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key = True)
    pavadinimas = Column("pavadinimas", String)
    adresas = Column("adresas", String)
    banko_kodas = Column("banko_kodas", String)
    swift_kodas = Column("SWIFT_kodas", String)
    saskaitos = relationship("Saskaita", back_populates = "bankas")

    def __init__(self, pavadinimas, adresas, banko_kodas, swift_kodas):
        self.pavadinimas=pavadinimas
        self.adresas=adresas
        self.banko_kodas=banko_kodas
        self.swift_kodas=swift_kodas

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas}, {self.adresas}, {self.banko_kodas}, {self.swift_kodas})"


            # Tarpine lentele
class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key = True)
    sask_numeris = Column("sask_numeris", String)
    balansas = Column("balansas_eur", Integer)
    asmuo_id = Column("asmuo_id", Integer, ForeignKey("asmuo.id"))
    bankas_id = Column("bankas_id", Integer, ForeignKey("bankas.id"))
    bankas = relationship("Bankas" , back_populates = "saskaitos")
    asmuo = relationship("Asmuo", back_populates = "saskaitos")

    def __init__(self, sask_numeris, balansas):
        self.sask_numeris=sask_numeris
        self.balansas=balansas

    def __repr__(self):
        return f"({self.id}, {self.sask_numeris}, {self.balansas})"
        
if __name__ == "__main__":
    Base.metadata.drop_all(engine)  # delete lenteles
    Base.metadata.create_all(engine)  # sukurti leneles



# # Pirmas variantas

# # Tarpine lentele
# saskaita_table = Table("saskaita", Base.metadata,
# Column("asmuo_id", Integer, ForeignKey("asmuo.id")),
# Column("bankas_id", Integer, ForeignKey("bankas.id")),
# Column(String, saskaita = "saskaita"),
# Column(Integer, balansas = "balansas_Eur")
# )

# # Asmuo class
# bankai = relationship(
#         "Bankas", 
#         secondary = saskaita_table, 
#         back_populates = "asmenys")

# # Bank class
# asmenys = relationship(
#     "Asmuo",
#     secondary = saskaita_table,
#     back_populates = "bankai"
# )