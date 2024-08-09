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
username = input("Zadejte přihlašovací jméno: ") # vloží username heslo a musím ověřit, zda se nachází v dictu. Když ne, vypíšu hlášku a vyzvu ho znovu a program ukončím.
password = input("Zadejte heslo: ")

def verify_user(username, password):
    """
    Ověří, zda zadané vstupy username a password jsou registrované a zda vzájemně tvoří login do aplikace
    """
    if username in registered and registered[username] == password:
        return True
    else:
        return False

if verify_user(username, password):
    print(f"Vítej v textovém analyzátoru, {username}!")
    from texty import TEXTS # importuji texty z externího souboru
    text_1 = TEXTS[0]
    text_2 = TEXTS[1]
    text_3 = TEXTS[2]
    print("=" * 50)
    print("VYBER SI TEXT K ANALÝZE")
    print("=" * 50)
    print("Text 1:", sep="\n")
    print(text_1)
    print("-" * 50)
    print("Text 2:", sep="\n")
    print(text_2)
    print("-" * 50)
    print("Text 3:", sep="\n")
    print(text_3)
    print("=" * 50)
else:
    print("Špatný login. Zkuste to znova. Program se nyní ukončí")

vstup = int(input("Zadejte číslo textu k analýze (1 - 3)"))
if vstup == 1:
    vybrany_text = TEXTS[0]
elif vstup == 2:
    vybrany_text = TEXTS[1]
elif vstup == 3:
    vybrany_text = TEXTS[3]
else:
    vybrany_text = None
    print("Neplatná volba. Zadejte číslo 1, 2 nebo 3.")
if vybrany_text:
    print("Zvolili jste následující text:")
    print(vybrany_text)