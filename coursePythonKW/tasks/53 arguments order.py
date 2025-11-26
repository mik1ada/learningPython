# Zadanie: Rezerwacja biletów na koncert
#
# Cel: Napisz program, który pozwoli użytkownikowi zarezerwować bilety na koncert.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję bookTickets, która przyjmuje nazwę zespołu jako argument
#    pozycyjny (band), liczbę biletów jako argument pozycyjny, a rodzaj biletów i sekcję
#    jako argumenty nazwane z domyślnymi wartościami jako standard i general
# 2) Funkcja powinna wyświetlać informacje o rezerwacji, włączając w to wszystkie
#    podane detale.
# 3) Poproś użytkownika o wprowadzenie nazwy zespolu i liczby bieltów,
#    następnie tylko je przekaż przy wywołaniu funkcji.

def bookTickets(band, numberOfTickets, /,* , typeOfTickets = 'standard', section = 'general'):
  print("Rezerwacja biletow")
  print("Zespol:", band)
  print("Liczba biletow:", numberOfTickets)
  print("Rodzaj biletow:", typeOfTickets)
  print("Sekcja:", section)

band = input("Podaj nazwe zespolu: ")
tickets = int(input("Podaj liczbe biletow: "))

bookTickets(band, tickets)