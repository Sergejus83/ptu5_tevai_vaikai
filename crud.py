from modelis import engine, Tevas, Vaikas
# .orm modulis --> sessionmaker 
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()


def create_tevas(vardas, pavarde):
    tevas = Tevas(vardas=vardas, pavarde=pavarde)
    session.add(tevas)
    session.commit()
    return tevas

def read_tevai():
    tevai = session.query(Tevas).all()
    return tevai

def update_tevas(tevas_id, **kwargs):
    tevas = session.query(Tevas).get(tevas_id)
    if tevas:
        if "vardas" in kwargs:
            tevas.vardas = kwargs["vardas"]
        if "pavarde" in kwargs:
            tevas.pavarde = kwargs["pavarde"]
        session.commit()
    else:
        print(f"Klaida: tevas su ID:{tevas_id} neegzistoja")

def delete_tevas(tevas_id):
    tevas = session.query(Tevas).get(tevas_id)
    if tevas:
        session.delete(tevas)
        session.commit()
        return True
    else:
        print(f"Klaida: tevas su ID:{tevas_id} neegzistoja")


def create_vaikas(vardas, pavarde, tevas, mokymo_istaiga=None):
    vaikas=Vaikas(
        vardas=vardas,
        pavarde=pavarde,
        tevas=tevas,
        mokymo_istaiga=mokymo_istaiga
    )
    session.add(vaikas)
    session.commit()
    return vaikas

def read_vaikai():
    return session.query(Vaikas).all()



if __name__=="__main__":
#Naujas Vaikas
    # tevas=session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas(
    #     "Arina", 
    #     "Bykova", tevas, 
    #     "Sofijos Kovalevskajos")
    # print(read_tevai(), read_vaikai())

    print(read_vaikai())

#Tevas
    # naujas_tevas = create_tevas("Sergejus", "Bykovas")
    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)
    # print(update_tevas(7, vardas="Labai", pavarde="Geras"))
    # print(delete_tevas(4))
    # print(read_tevai())

