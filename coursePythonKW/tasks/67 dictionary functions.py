# Zadanie - zarządzanie książką adresową
# W tym zadaniu będziesz używać słowników do zarządzania prostą
# książką adresową. Nauczysz się dodawać, usuwać, kopiować oraz
# przeszukiwać dane w słowniku.
#
# 1) Stwórz słownik `addressBook` zawierający początkowo jedną
#    osobę: Jan Kowalski, mieszka w Gdańsku, kod pocztowy 80-000.
# 2) Dodaj do książki adresowej nową osobę: Anna Nowak, mieszka w
#    Warszawie, kod pocztowy 00-001.
# 3) Usuń Jan Kowalski z książki adresowej.
# 4) Skopiuj książkę adresową do nowej zmiennej i sprawdź, czy
#    kopia jest identyczna (porównaj referencje i zawartość).
# 5) Sprawdź, czy w skopiowanej książce adresowej jest osoba
#    mieszka w Krakowie. Jeśli nie, wyświetl odpowiedni komunikat.
# 6) Wyświetl wszystkie klucze i wartości w książce adresowej.

addressBook = {
  'Jan Kowalski': {
  'city': 'Gdansk',
  'postalcode': '00-001'
  },
}

print(addressBook)

addressBook['Anna Nowak'] = {'city': 'Warszawa', 'postalcode': '00-001'}

del addressBook['Jan Kowalski']

copyAddressBook = addressBook.copy()

print(copyAddressBook is addressBook)
print(copyAddressBook['Anna Nowak'] is addressBook['Anna Nowak'])

for person in addressBook.values():
  if person['city'] == 'Krakow':
    print("W ksiazce jest osoba z krakowa")
  else:
    print("W ksiazce nie ma osoby z krakowa")

print("Klucze ksiazki adresowej:", addressBook.keys())
print("Wartosci ksiazki adresowej:", addressBook.values())