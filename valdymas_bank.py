from sqlalchemy.orm import sessionmaker
from models_bank import engine, Asmuo, Bankas, Saskaita
from pprint import pprint

Session = sessionmaker(bind=engine)
session = sessionmaker(engine)()


# asmuo = Asmuo(vardas = "Sergejus", pavarde = "Bykovas", asm_kodas = 38301050000, tel_numeris = 861234567)

# įvesti asmenis, bankus, sąskaitas. Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų. 
# Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

def create_asmuo(): #(vardas, pavarde...)
    # asmuo = Asmuo(vardas=vardas, pavarde=pavarde...)
    #    session.add(asmuo)
    #     session.commit()
    #     print(f" ...
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
        print_all_banks()
        bankas_id = int(input("ivesti banko ID: "))
        print_all_persons()
        asmuo_id = int(input("ivesti asmens ID: "))
    except ValueError:
        print("Klaida: ivestas ne skaicius")
        return None
    else:
        saskaita = Saskaita(sask_numeris, balansas)
        saskaita.bankas_id = bankas_id
        saskaita.asmuo_id = asmuo_id
        session.add(saskaita)
        session.commit()
        print(f"naujas sasskaita: '{sask_numeris}' sameniui su ID: '{asmuo_id}' sukurta sekmingai!")

def account_info():
    pass

def add_incom_to_account():
    # print_all_persons()
    print_all_accounts()
    saskaita_id = int(input("ivesti saskaitos ID: "))
    pasirinkta_saskaita = session.query(Saskaita).get(saskaita_id)
    pajamas = float(input("Iveskite pajamas: "))
    pasirinkta_saskaita.balansas += pajamas
    session.commit()
    print("Jusu balansas pakeistas")
    print_all_accounts()

def add_expenses_to_account():
    print_all_accounts()
    saskaita_id = int(input("ivesti saskaitos ID: "))
    pasirinkta_saskaita = session.query(Saskaita).get(saskaita_id)
    islaidos = float(input("ivesti islaidos: "))
    pasirinkta_saskaita.balansas -= islaidos
    session.commit()
    print("Jusu balansas pakeistas")
    print_all_accounts()

def print_all_persons():
    asmenys = session.query(Asmuo).all()
    for asmuo in asmenys:
        print("visi asmenys: ", asmuo)

def print_all_banks():
    bankai = session.query(Bankas).all()
    for bankas in bankai:
        print("visi bankai: ", bankas)

def print_all_accounts():
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
            add_incom_to_account()
        if pasirinkimas == "2":
            add_expenses_to_account()
        if pasirinkimas == "3":
            pass
        if pasirinkimas == "9":
            print("Pagrindinis menu")
    if pasirinkimas == "5":
        print_all_persons()
    if pasirinkimas == "6":
        print_all_banks()
    if pasirinkimas == "7":
        print_all_accounts()
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
