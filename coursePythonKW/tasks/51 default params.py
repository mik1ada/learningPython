# Funkcja z domyślnymi wartościami parametrów
# 1) Napisz funkcję z parametrami:
#    - email
#    - country z domyślną wartością "Polska"
#    - company z domyślną wartością "Example Ltd"
# 2) Zwróć z funkcji słownik z elementami jak parametry 
# 3) Przetestuj funkcję z jednym argumentem ola@example.com
#    oraz drugi przypadek z kasia@example.com będąca z UK

def exampleFunc(email, country = "Polska", company = "Example Ltd"):
  dict = {
    'email': email,
    'country': country,
    'company': company
  }
  return dict

test1 = exampleFunc("ola@example.com")
test2 = exampleFunc("kasia@example.com", "UK")
print(test1)
print(test2)