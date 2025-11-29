# Zadanie: Przetwarzanie danych użytkowników 
# Cel: Napisz program do przetwarzania danych użytkowników z listy.  
#
# Kroki do wykonania:
# 1) Stwórz listę słowników users, gdzie każdy słownik zawiera klucze 'name' i 'age'
#    z przykładowymi danymi użytkowników.
# 2) Użyj filter do wyfiltrowania użytkowników, którzy mają więcej niż 18 lat.
# 3) Użyj map do podwojenia wieku przefiltrowanych użytkowników.
# 4) Użyj reduce do zsumowania wszystkich lat po przetworzeniu.
# 5) Wyświetl sumę lat przefiltrowanych i przetworzonych użytkowników.
#
# Rozwiązanie:

from functools import reduce

user1 = {
  'name': 'ania',
  'age': 18
}

user2 = {
  'name': 'basia',
  'age': 34
}

user3 = {
  'name': 'zbigniew',
  'age': 47
}

users = [user1, user2, user3]

olderThan18 = filter(lambda user: user['age'] > 18, users)
doubledAge = list(map(lambda user: user['age'] * 2, olderThan18))
sumOfYears = reduce(lambda x, y: x + y, doubledAge)

print(sumOfYears)