# 1. Stwórz listę data z kolejnymi liczbami: od 0 do 6
# 2. Pokaż w konsoli długość listy, skasuj 2 element
#    i pokaż długość listy ponownie
# 3. Użyj instrukcji warunkowej if z in do sprawdzenia czy
#    liczba 3 jest w liście data, pokaż informację 
#    w konsoli jeśli zachodzi taka sytuacja. Przykład:
#    if 100 in someList:
#       print("100 jest w liście")
# 4. Użyj pętli for aby pokazać wartości w liście.
#    for el in someList:
#       print("element listy z dodaną wartością 2", el + 2)
# 5. Użyj pętli for aby przejść po elementach listy, ale
#    pokaż ich wartości pomnożone przez 2x

data = list(range(7))

print("Dlugosc listy:", len(data))
del data[1]
print("Dlugosc listy po usunieciu 2 elementu:", len(data))

if 3 in data:
  print("Liczba 3 jest w liscie data")

for element in data:
  print(f"Element listy: {element}")

for element in data:
  print(f"Wartosc elementu pomnozona przez 2: {element * 2}")

