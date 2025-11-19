# Zadanie - operacje na rachunku bankowym, skorzystaj 
# z skróconych operatorów przypisania z operacją
# matematyczną np:  +=  -=  *=  /=  itd
# Uwaga, po każdej operacji wyświetl saldo w konsoli
# 1) Stwórz zmienną balance z wartością początkową 1000
# 2) Dodaj wartość nowej pensji 7000
# 3) Odejmij 2000 kosztów za mieszkanie
# 4) Błąd banku pomnożył Twoje saldo trzykrotnie
# 5) Odejmij 4000 na komputer
# 6) Bank zorientował się że powstał błąd i cofa ostatnie           
#    transakcje. Dodaj do salda 4000, podziel je przez 3
#    i dopiero teraz odejmij 4000
# 7) Pokaż saldo końcowe

balance = 1000

pensja = 7000
balance += pensja
print("Aktualny stan salda wynosi:", balance)

kosztMieszkania = 2000
balance -= kosztMieszkania
print("Aktualny stan salda wynosi:", balance)

błądBanku = 3
balance *= błądBanku
print("Aktualny stan salda wynosi:", balance)

kosztKomputera = 4000
balance -= kosztKomputera
print("Aktualny stan salda wynosi:", balance)

balance += kosztKomputera
balance /= błądBanku
balance -= kosztKomputera

print("Saldo koncowe wynosi:", balance)
