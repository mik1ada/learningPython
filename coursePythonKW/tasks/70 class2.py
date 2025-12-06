# Zadanie - zarządzanie kontem użytkownika
# W tym zadaniu stworzysz prostą klasę reprezentującą konto użytkownika.
# Będziesz zarządzać podstawowymi informacjami o użytkowniku oraz umożliwić zmianę hasła.
#
# 1) Stwórz klasę User, która w konstruktorze przyjmuje dwa parametry:
#    username (nazwa użytkownika) i password (hasło). Zapisz te wartości jako atrybuty obiektu.
# 2) Dodaj metodę changePassword, która przyjmuje dwa argumenty:
#    oldPassword (stare hasło) i newPassword (nowe hasło). Sprawdź, czy stare hasło
#    zgadza się z obecnym hasłem użytkownika. Jeśli tak, zmień hasło na nowe.
# 3) Stwórz instancję klasy User z przykładowym użytkownikiem.
# 4) Spróbuj zmienić hasło użytkownika za pomocą metody changePassword.
#    Najpierw użyj nieprawidłowego starego hasła, a następnie prawidłowego.

class User:
  def __init__(self, username, password) -> None:
    self.username = username
    self.password = password
  
  def changePassword(self, oldPassword, newPassword):
    if oldPassword == self.password:
      self.password = newPassword

maciek = User('maciek2020', '123XD')
print(maciek.password)
maciek.changePassword('123DX', '123DX')
print(maciek.password)
maciek.changePassword('123XD', '123DX')
print(maciek.password)