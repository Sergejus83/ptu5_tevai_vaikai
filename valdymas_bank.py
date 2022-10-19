from sqlalchemy.orm import sessionmaker
from models_bank import engine, Asmuo, Bankas, Saskaita
from pprint import pprint

Session = sessionmaker(bind=engine)
session = sessionmaker(engine)()


# asmuo = Asmuo(vardas = "Sergejus", pavarde = "Bykovas", asm_kodas = 38301050000, tel_numeris = 861234567)

# įvesti asmenis, bankus, sąskaitas. Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų. 
# Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

def create_asmuo():
    try:
        vardas = input("vardas: ")
        pavarde = input("pavarde: ")
        asm_kodas = int(input("asmens kodas: "))
        tel_numeris = int(input("telefono numeris: "))
    except ValueError:
        print("Klaida: ivestas ne skaicius")
        return None
    else:
        asmuo = Asmuo(vardas, pavarde, asm_kodas, tel_numeris)
        session.add(asmuo)
        session.commit()
        print(f" --- naujas asmuo: '{vardas} {pavarde}' sukurtas sekmingai! ---")

def create_bankas():
        pavadinimas = input("pavadinimas: ")
        adresas = input("adresas: ")
        banko_kodas = input("banko kodas: ")
        swift_kodas = input("SWIFT kodas: ")
        bankas = Bankas(pavadinimas, adresas, banko_kodas, swift_kodas)
        session.add(bankas)
        session.commit()
        print(f" --- naujas bankas: '{pavadinimas}' sukurtas sekmingai! ---")

def create_saskaita():
    try:
        sask_numeris = input("saskaitos numeris: ")
        balansas = 0
    except ValueError:
        print("Klaida: ivestas ne skaicius")
        return None
    else:
        saskaita = Saskaita(sask_numeris, balansas)
        session.add(saskaita)
        session.commit()
        print(f"naujas sasskaita: '{sask_numeris}' sukurta sekmingai!")

def sask_info():
    pass

def read_all_asmuo():
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        print("visi asmenys: ", asmuo)

def read_all_bankas():
    bankai = session.query(Bankas).all()
    for bankas in bankai:
        print("visi bankai: ", bankas)

def read_all_saskaita():
    saskaitos = session.query(Saskaita).all()
    for saskaita in saskaitos:
        print("visos saskaitos: ", saskaita)




while True:
    print("Prasau ivesti norima pasirinkima: ")
    pasirinkimas = input(" 1 - ivesti asmeni\n 2 - ivesti banka\n 3 - iveskite saskaita\n 4 - sakaitos info\n\
 5 - perziureti visus asmenius\n 6 - perziureti visus bankus\n 7 - perziureti visas saskaitas\n 0 - exit\n Jusu pasirinkimas: ")
    if pasirinkimas == "1":
        create_asmuo()
    if pasirinkimas == "2":
        create_bankas()
    if pasirinkimas == "3":
        create_saskaita()
    if pasirinkimas == "4":
        pasirinkimas = input(" 1 - ivesti pajamas\n 2 - ivesti islaidas\n 3 - perziureti balansa\n\
 9 - grizti i pagrindine Meniu\n Jusu pasirinkimas: ")
        if pasirinkimas == "1":
            pass
        if pasirinkimas == "2":
            pass
        if pasirinkimas == "3":
            pass
        if pasirinkimas == "9":
            print("Pagrindine menu")
    if pasirinkimas == "5":
        read_all_asmuo()
    if pasirinkimas == "6":
        read_all_bankas()
    if pasirinkimas == "7":
        read_all_saskaita()
    if pasirinkimas == "0":  
        break
    





# def create_object(Asmuo, **kwargs):
#     asmuo = Asmuo(**kwargs)
#     session.add(asmuo)
#     session.commit()
#     return asmuo

# def create_asmuo(Asmuo, **kwargs):
#     asmuo = Asmuo(**kwargs)
#     session.add(asmuo)
#     session.commit()
#     return asmuo
