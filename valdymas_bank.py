from sqlalchemy.orm import sessionmaker
from models_bank import engine, Asmuo, Bankas, Saskaita

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


while True:
    print("Prasau ivesti norima pasirinkima: ")
    pasirinkimas = input(" 1 - ivesti asmeni\n 2 - ivesti banka\n 3 - iveskite saskaita\n 4 - sakaitos info\n\
 5 - perziureti visus asmenius\n 6 - perziureti visus bankus\n 7 - perziureti visas saskaitas\n 0 - exit\n Jusu pasirinkimas: ")
    if pasirinkimas == "1":
        # vardas = input("vardas: ")
        # pavarde = input("pavarde: ")
        # asm_kodas = input("asmens kodas: ")
        # tel_numeris = input("telefono numeris: ")
        # asmuo = Asmuo(vardas=vardas, pavarde=pavarde, asm_kodas=asm_kodas, tel_numeris=tel_numeris)
        # session.add(asmuo)
        # session.commit()
        create_asmuo()
    if pasirinkimas == "2":
        create_bankas()
    if pasirinkimas == "3":
        create_saskaita()

    if pasirinkimas =="0":  
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
