"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Peter Tlučhoř

email: tluchor.peter@outlook.com

discord: Tlucek#0754

"""

# Nejdřív musím vytvořit databázi registrovaných uživatelů a jejich hesel. Jelikož se jedná o páry klíč+hodnota, vytvořím dict.
registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
username = input("Zadejte přihlašovací jméno: ") # vloží username a musím ověřit, zda se nachází v dictu. Když ne, vypíšu hlášku a vyzvu ho znovu.
password = input("Zadejte heslo: ")

def verify_user(username, password):
    if username in registered and registered[username] == password:
        return True
    else:
        return False

if verify_user(username, password):
    print(f"Vítej v textovém analyzátoru, {username}!")
else:
    print("Špatný login. Zkuste to znova. Program se nyní ukončí")