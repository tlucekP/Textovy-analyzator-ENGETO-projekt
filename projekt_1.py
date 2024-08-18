"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Peter Tlučhoř
email: tluchor.peter@outlook.com

discord: Tlucek#0754

"""

from texty import TEXTS # importuji texty z externího souboru
import string # v analýze použiju modul string s proměnnou punctuation pro identifikaci interpunkčních znamének k očištění ve slovech

# Nejdřív musím vytvořit databázi registrovaných uživatelů a jejich hesel. Jelikož se jedná o páry klíč+hodnota, vytvořím dict.
registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

def main(): # celou analýzu textu zadefinuji do main funkce
    vybrany_text = input("Zadejte číslo textu k analýze (1 - {}): ".format(len(TEXTS))) # využiji dynamický rozsah vstupu, kdyby v budoucnu přibyl další text
    print("=" * 55)
    if vybrany_text.isdigit(): # podmíním uživatelský vstup vložením čísla
        vybrany_text = int(vybrany_text)
    else:
        print("Vložte číslo! Program se nyní ukončí. Zkuste to, prosím, znovu.")
        return
    
    if vybrany_text-1 < 0 or vybrany_text > len(TEXTS):
        print(f"Text číslo {vybrany_text} neexistuje. Zkuste to, prosím, znovu.")
        return
    
    # očistím slova o nežádoucí interpunkční znaky v jedné proměnné, aby nemusel pořád procházet slova v jednotlivých podmínkách
    translator = str.maketrans("", "", string.punctuation)
    slova = TEXTS[vybrany_text-1].translate(translator).split()

    counter = { # předpřipravený dict pro statistiku
        "vsechnaslova": 0,
        "Slova": 0,
        "SLOVA": 0,
        "slova": 0,
        "cisla": 0,
        "sum": 0,
        "lenstat": {}
    }

    for slovo in slova: # iteruji text pro statistiku. Čísla definuji jako float, kdyby se tam float vyskytovalo. Využívám try-except.
        slovo_delka = len(slovo)
        try:
            cislo = float(slovo)
            counter["cisla"] += 1
            counter["sum"] += cislo
        except ValueError:
            pass
        counter["vsechnaslova"] +=1
        if slovo_delka in counter["lenstat"]:
            counter["lenstat"][slovo_delka] += 1
        else:
            counter["lenstat"][slovo_delka] = 1
        if slovo.isupper():
            counter["SLOVA"] += 1
        if slovo.islower():
            counter["slova"] += 1
        if slovo[0].isupper():
            counter["Slova"] += 1
                    
    print(f"Ve vybraném textu je {counter['vsechnaslova']} slov.")
    print(f"Ve vybraném textu je {counter['Slova']} začínajících velkým písmenem.")
    print(f"Ve vybraném textu je {counter['SLOVA']} slov obsahující všechna písmena velká.")
    print(f"Ve vybraném textu je {counter['slova']} slov obsahující všechna písmena malá.")
    print(f"Ve vybraném textu je {counter['cisla']} počet čísel.")
    print(f"Ve vybraném textu je {counter['sum']} součtem všech čísel.")

    max_frekvence = max(counter["lenstat"].values(), default=0) # max počet hvězdiček pro sloupec OCCURENCES
    max_occurences = max(15, max_frekvence) # šířka sloupce OCCURENCES, musím zvolit dynamické zadání, protože nevím jak velká slova tam jsou

    print(f"\nLEN| {'OCCURENCES'.center(max_occurences)} |NR") # jelikož tam můžou být různě dlouhá slova, musím použít formátování dle max_occurences

    for delka, frekvence in sorted(counter["lenstat"].items()):
        print(f"{delka:<3}| {'*' * frekvence:<{max_occurences}} |{frekvence:<2}") # využívám dynamické formátování textu při výpisu

def verify_user(username, password):
    """
    Ověří, zda zadané vstupy username a password jsou registrované a zda vzájemně tvoří login do aplikace
    """
    return username in registered and registered[username] == password

def kontrola_vstupu(value):
    """Kontroluje, zda vstupní hodnota je integer v rozmězí 1-3."""
    return value.isdigit() and 1 <= int(value) <= len(TEXTS)

if __name__ == "__main__":
    username = input("Zadejte přihlašovací jméno: ")
    password = input("Zadejte heslo: ")

    if verify_user(username, password):
        print(f"Vítej v textovém analyzátoru, {username}!")
        print("=" * 55)
        main()
    else:
        print("Špatný login. Zkuste to znova. Program se nyní ukončí.")
