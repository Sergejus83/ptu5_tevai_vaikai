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

def delete_object(object_class, object_id):
    obj = session.query(object_class).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    else:
        print(f"Klaida:{object_class.__name__} su ID {object_id} neegzistoja")

def update_object(object_class, object_id, **kwargs):
    obj = session.query(object_class).get(object_id)
    if obj:
        if obj and kwargs:
            for column_name, value in kwargs.items():
                if hasattr(obj, column_name):
                    setattr(obj, column_name, value)
                else:
                    print(f"Klaida:{obj} neturi {column_name} atributo")
            else:
                session.commit()
                return obj
        else:
            print(f"Klaida:{object_class.__name__} su ID {object_id} neegzistoja")


if __name__=="__main__":
#ivaikinimas
    vaikas = session.query(Vaikas).filter(Vaikas.pavarde.ilike("Super%")).first()
    tevas = session.query(Tevas).filter(Tevas.pavarde.ilike("Bykov%")).first()
    ivaikintas = update_object(Vaikas, vaikas.id, tevas=tevas, vardas = "ivaikintas")   
    print("Python objektas ivaikintas: \n", ivaikintas)
    print("Perkraunam is DB: \n", read_vaikai())

    #sukuriam 
    # naujas_tevas = create_tevas("Hello", "Hi")
    # naujas_vaikas = create_vaikas("Super", "Supervaikas", naujas_tevas)
    # print(read_vaikai())
    # delete_object(Tevas, naujas_tevas.id)
    # print("read vaikai \n", read_vaikai())
































#Naujas Vaikas
    # tevas=session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas(
    #     "Daniil", 
    #     "Bykov", tevas, 
    #     "Vilniaus Sofijos Kovalevskajos progimnazija")
    # # print(read_tevai(), read_vaikai())

    # print(read_vaikai())

#Tevas
    # naujas_tevas = create_tevas("Sergejus", "Bykovas")
    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)
    # update_tevas(1, vardas="Sergejus", pavarde="Bykovas")
    # print(delete_tevas(4))
    # print(read_tevai())

