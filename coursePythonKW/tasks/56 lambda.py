# Zadanie z lambdą i map
# 1) Stwórz listę names z wartościami: Ola, Ania, Kasia
# 2) z pomocą mapy i lambdy dodaj do każdego imienia tekst " Kowalska"
# 3) Wyświetl nową listę w konsoli
# 4) Przefiltruj nową listę ze względu na długość tekstu, zachowaj
#    w nowej liście tylko te które mają więcej niż 12 znaków
#    Pokaż przefiltrowaną listę w konsoli

names = ['Ola', 'Ania', 'Kasia']
names2 = list(map(lambda x: x + " Kowalska", names))

print(names2)

names2 = list(filter(lambda x: len(x) > 12, names2))
print(names2)