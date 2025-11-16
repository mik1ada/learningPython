# Zadania z for i range
# 1) Stwórz zmienną sum, która będzie miała ustawioną wartość 0 przed każdą pętlą
# 2) Zrób pętlę for z wartościami od 0 do 200 z range, zsumuj liczby i wyświetl
#    rezultat w konsoli
# 3) Zrób pętlę for z range z liczbami od 50 do 100, dodaj je i wyświetl wynik
# 4) Zrób kolejną pętlę z range od 0 do 300 z krokiem co 3, dodaj liczby
#    i wyświetl wynik w konsoli

sum = 0

for number in range(0,201):
  sum += number

print("Suma od 0 do 200 wynosi: ", sum)

sum = 0

for number in range(50,101):
  sum += number

print("Suma od 50 do 100 wynosi:", sum)

sum = 0

for number in range(0,301,3):
  sum += number

print("Suma od 0 do 300 co 3 wynosi:", sum)