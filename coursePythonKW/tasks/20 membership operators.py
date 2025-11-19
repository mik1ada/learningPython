# Zadanie do wykonania:
# Wykorzystaj operatory przynależności (in, not in) do sprawdzenia
# obecności elementów w kolekcjach i użycie instrukcji warunkowej if.
# 1) Sprawdź, czy liczba 7 znajduje się w liście 'numbers' i wyświetl odpowiedni komunikat.
# 2) Sprawdź, czy ciąg znaków "kot" nie znajduje się w tuple 'animals' i wyświetl odpowiedni komunikat.
# 3) Stwórz słownik 'user' z kluczami 'name' i 'age'. Sprawdź, czy klucz 'name' znajduje się w słowniku.
# 4) Jeśli w liście 'numbers' jest liczba 3, zwiększ jej wartość o 2 i wyświetl nową listę.
#    Użyj pętli for i instrukcji warunkowej if.

numbers = list(range(0,9))

if 7 in numbers:
  print("7 w liscie")
else:
  print("7 nie ma w liscie")

animals = ("pies", "ryba", "kot")

if 'kot' not in animals:
  print("Kot nie jest w krotce")
else:
  print("Kot jest w krotce")

user = {
  'name': 'Jan',
  'age': 18
}

if 'name' in user:
  print("Taki klucz znajduje sie w slowniku")
else:
  print("Brak klucza 'name' w slowniku")

for i in range(len(numbers)):
  if numbers[i] == 3:
    numbers[i] += 2

print(numbers)
