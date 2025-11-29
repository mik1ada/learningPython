# Zadanie: Zarządzanie stanem konta użytkownika
#
# Cel: Napisz program do zarządzania stanem konta użytkownika, który pozwala na
# dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program
# powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz
# zawierać funkcje do modyfikacji tego stanu i wyświetlania go. 
#
# Kroki do wykonania:
# 1) Zdefiniuj globalną zmienną accountBalance z wartością początkową 0.
# 2) Napisz funkcję addFunds, która przyjmuje kwotę do dodania do konta.
#    Funkcja ta powinna modyfikować globalną zmienną accountBalance.
# 3) Napisz funkcję withdrawFunds, która przyjmuje kwotę do wypłaty z konta.
#    Sprawdź, czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat.
# 4) Napisz funkcję displayBalance, która wyświetla aktualny stan konta.
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu)
#    i odpowiednio zareaguj, wywołując odpowiednią funkcję.
#
# Rozwiązanie:

accountBalance = 0

def addFunds(additionalBalance):
  global accountBalance 
  accountBalance += additionalBalance

def withdrawFunds(withdrawedBalance):
  global accountBalance
  if withdrawedBalance <= accountBalance:
    accountBalance -= withdrawedBalance
  else:
    print("Nie ma wystarczajacych srodkow na koncie aby zrealizowac wyplate")

def displayBalance():
  global accountBalance
  print("Aktualny stan konta wynosi:", accountBalance)

while True:
  action = input("Podaj działanie, które chcesz wykonać[wplata, wyplata, stan, koniec]:")
  if action.lower() == 'koniec':
    break
  elif action.lower() == 'wplata':
    additionalBalance = float(input("Podaj kwote ktora chcesz wplacic:"))
    addFunds(additionalBalance)
  elif action.lower() == 'wyplata':
    withdrawedBalance = float(input("Podaj kwote ktora chcesz wyplacic:"))
    withdrawFunds(withdrawedBalance)
  elif action.lower() == 'stan':
    displayBalance()
  else:
    print("Podano inna akcje niz mozliwe do wybrania")
