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

def chose_account_id():
    pass

def account_info():
    print_all_accounts()
    saskaita_id = int(input("ivesti saskaitos ID: "))
    pasirinkta_saskaita = session.query(Saskaita).get(saskaita_id)
    pasirinktas_balansas = pasirinkta_saskaita.balansas
    print("sakaitos info: ", pasirinktas_balansas)

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
    pasirinkimas = input(" 1 - Meniu 'ivesti'\n 2 - Meniu 'pajamas/islaidas'\n 3 - Meniu 'perziura'\n 0 - exit\n Jusu pasirinkimas: ")
    if pasirinkimas == "0":  
        break
    if pasirinkimas == "1":
        print(" -- meniu 'ivesti' -- ")
        pasirinkimas = input(" 1 - ivesti asmeni\n 2 - ivesti banka\n 3 - iveskite saskaita\n 0 - grizti i Meniu\n Jusu pasirinkimas: ")
        if pasirinkimas == "1": 
            create_asmuo()
        if pasirinkimas == "2":
            create_bankas()
        if pasirinkimas == "3":
            create_saskaita()
        if pasirinkimas == "0":
            print("Meniu")
    if pasirinkimas == "2":
        print(" -- meniu 'pajamos/islaidos' -- ")
        pasirinkimas = input(" 1 - ivesti pajamas\n 2 - ivesti islaidas\n 3 - perziureti balansa\n 0 - grizti i Meniu\n Jusu pasirinkimas: ")
        if pasirinkimas == "1":
            add_incom_to_account()
        if pasirinkimas == "2":
            add_expenses_to_account()
        if pasirinkimas == "3":
            account_info()
        if pasirinkimas == "0":
            print("Meniu")
    if pasirinkimas == "3":
        print(" -- meniu 'perziura' -- ")
        pasirinkimas = input(" 1 - perziureti visus asmenius\n 2 - perziureti visus bankus\n 3 - perziureti visas saskaitas\n 0 - grizti i Meniu\n Jusu pasirinkimas: ")
        if pasirinkimas == "1":
            print_all_persons()
        if pasirinkimas == "2":
            print_all_banks()
        if pasirinkimas == "3":
            print_all_accounts()
        if pasirinkimas == "0":
            print("Meniu")

    

# def create_asmuo(Asmuo, **kwargs):
#     asmuo = Asmuo(**kwargs)
#     session.add(asmuo)
#     session.commit()
#     return asmuo
