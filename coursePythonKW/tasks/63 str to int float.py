# Zadanie na Number:
# 1) pobierz liczbę całkowitą od użytkownika do zmiennej
#    za pomocą funkcji input, przekaż do niej informację: Podaj liczbę całkowitą.
# 2) Zmień typ wartości z tekstu na liczbę całkowitą 
# 3) Stwórz funkcję calculateSquareArea z parametrem height
#    która zwraca powierzchnią kwadratu.
# 4) Wywołaj funkcję z wcześniej pobraną liczbą całkowitą,
#    wynik pokaż w konsoli.
# 5) Pobierz od użytkownika liczbę dziesiętną, pamiętaj o kropce
#    w liczbie. Oblicz powierzchnię kwadratu z tą wartością,
#    pokaż wynik w konsoli zaokrąglony do 2 miejsc po przecinku. 

def calculateSquareArea(height):
  squareArea = height ** 2
  return squareArea

number = int(input("Podaj liczbe calkowita:"))

print(calculateSquareArea(number))

floatNumber = float(input("Podaj liczbe dziesietna:"))
squareArea = calculateSquareArea(floatNumber)
print(round(squareArea, 2))