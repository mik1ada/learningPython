# String i find()
# 1) Napisz funkcję validateEmail sprawdzającą w podstawowy
#    sposób czy email jest prawidłowy.
# 2) Wykorzystaj find() do wyszukania fragmentów tekstu w email:
#    - sprawdź czy istnieje w przekazanym do funkcji emailu
#      znak @, zapisz index w monkeyIndex
#    - posiadając pozycję @ sprawdź czy istnieje znak 
#      kropki po małpie. Zapisz pozycję kropki w dotIndex
#    - jeżeli wszystkie powyższe warunki są spełnione
#      zwróć True, w innym wypadku False 
# 3) Wywołaj funkcję z następującymi mailami, pokaż
#    w konsoli co zwraca funkcja:
#    - asia@example.com 
#    - karol@domena 
#    - user.com

def validateEmail(email):
  monkeyIndex = None
  dotIndex = None
  monkeyPosition = email.find('@')
  if monkeyPosition > -1:
    monkeyIndex = email[monkeyPosition+1:]
    if monkeyIndex.find('.') > -1:
      dotIndex = monkeyIndex.find('.')
      return True
  return False

print(validateEmail('asia@example.com'))
print(validateEmail('karol@domena'))
print(validateEmail('user.com'))