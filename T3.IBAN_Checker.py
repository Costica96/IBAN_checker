#This aplication is a IBAN verificator.

IBAN_LENGHT = 24
AGREED_COUNTRY = { "RO" : "Romania", "FR" : "Franta", "ES" : "Spania", "PK" : "Pakistan"}
AGREED_BANK = { "BRE" : "Banca BRD", "RNC" : "Banca BCR", "ING" : "Banca ING", "UCB" : "Banca UniCredit"}

user_iban = input("Va rog sa introduceti codul dumneavoastra IBAN:\n ").upper()

if len(user_iban) == IBAN_LENGHT:
    if user_iban[0:2].isalpha():
        if user_iban[2:4].isnumeric():
            if user_iban[4:8].isalpha():
                if user_iban[8:24+1].isalnum():
                    print("Formatul IBAN-ului dumneavoastra este corect")
                    print(f"Tara dumneavoastra este {user_iban[0:2]}")
                    if user_iban[0:2] in AGREED_COUNTRY:
                        print(f"Noi am verificat tara {AGREED_COUNTRY[user_iban[0:2] ] } si este agreata de fondul monetar ")
                        print(f"Banca dumneavoastra este {user_iban[4:8]}")
                        if user_iban[4:7]:
                            print(f"{AGREED_BANK[user_iban[4:7]]} este agreata de fondul monetar")
                        else :
                            print("Aceasta banca nu este agreata")
                    else :
                        print("Nu sunteti dintr-o tara agreata de fondul monetar")
                else :
                    print("Verificati ultimile 16 caractere din IBAN")
            else :
                print("Verificati codul bancii din IBAN")
        else :
            print("Numarul de verificare din IBAN este gresit")
    else :
        print("Verificati codul tarii din care proveniti")
else :
    print("Codul IBAN este introdus gresit")







