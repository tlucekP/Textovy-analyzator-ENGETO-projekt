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
else:
    print("Špatný login. Zkuste to znova. Program se nyní ukončí")

from texty import TEXTS # importuji texty z externího souboru
text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2]
print("=" * 55)
print("VYBER SI TEXT K ANALÝZE")
print("=" * 55)

vybrany_text = None
while vybrany_text is None:
    vstup = int(input("Zadejte číslo textu k analýze (1 - 3): "))
    if vstup == 1:
        vybrany_text = TEXTS[0]
        break
    elif vstup == 2:
        vybrany_text = TEXTS[1]
        break
    elif vstup == 3:
        vybrany_text = TEXTS[2]
        break
else:
    print("Neplatná volba. Zadejte číslo 1, 2 nebo 3.")
print("Zvolili jste následující text:", sep="\n")
print("-" * 55)
print(vybrany_text)

slova = vybrany_text.split() #musím rozdělit slova v textu
pocet_slov = len(slova) # zjistím si počet slov
slova_velke_pismeno_tit = sum(1 for slovo in slova if slovo.istitle()) # počet slov začínající velkým písmenem
slova_velka_pismena = sum(1 for slovo in slova if slovo.isupper()) # počet slov obsahující velká písmena
slova_mala_pismena = sum(1 for slovo in slova if slovo.islower()) # počet slov obsahující malá písmena
pocet_cisel = sum(1 for slovo in slova if slovo.isdigit()) # počet čísel v textu
suma_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit()) # součet všech čísel v textu

print("-" * 55)
print(f"Ve vybraném textu je {pocet_slov} slov.")
print(f"Ve vybraném textu je {slova_velke_pismeno_tit} slov začínajících velkým písmenem.")
print(f"Ve vybraném textu je {slova_velka_pismena} slov obsahující všechna písmena velká.")
print(f"Ve vybraném textu je {slova_mala_pismena} slov obsahující všechna písmena malá.")
print(f"Ve vybraném textu je {pocet_cisel} počet čísel.")
print(f"Ve vybraném textu je součet všch čísel {suma_cisel}.")
print("-" * 55)
