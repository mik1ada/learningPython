# Zadanie: Kalkulator średniej arytmetycznej
#
# Cel: Napisz program kalkulatora, który oblicza średnią arytmetyczną z listy liczb.
# Program powinien używać funkcji lambda, map oraz reduce do przetworzenia listy liczb
# i obliczenia wyniku. Zadanie ma na celu praktyczne zastosowanie wyrażeń lambda
# i funkcji wyższego rzędu do przetwarzania danych. 
#
# Kroki do wykonania:
# 1) Zdefiniuj listę liczb, dla której ma zostać obliczona średnia arytmetyczna.
# 2) Użyj funkcji map i lambda do przekształcenia listy liczb, jeśli to konieczne.
# 3) Wykorzystaj funkcję reduce i lambda do obliczenia sumy wszystkich liczb z listy.
# 4) Oblicz średnią arytmetyczną dzieląc sumę przez ilość liczb w liście.
# 5) Wyświetl wynik.
#
# Rozwiązanie:

from functools import reduce

listOfNumbers = [23, 12, 11, 101]

sum = reduce(lambda x, y: x + y, listOfNumbers)
average = sum / len(listOfNumbers)
print(average)