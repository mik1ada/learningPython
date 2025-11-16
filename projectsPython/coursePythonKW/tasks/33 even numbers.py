# 1) Stwórz krotkę z wartościami od 1 do 10
# 2) Zrób pętle for in z krotką i wyświetl w konsoli
#    tylko parzyste liczby. Skorzytaj z instrukcji 
#    warunkowej if oraz operatora % zwracającego resztę
#    z dzielenia. Jeśli reszta z dzielenia przez 2
#    będzie równa 0 to nie ma reszty, tym samym liczba
#    jest parzysta

numbers = tuple(range(1,11))

for number in numbers:
  if number % 2 == 0:
    print(number, "to liczba parzysta")