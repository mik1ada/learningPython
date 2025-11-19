number = 5

while number > 0:
  print(number)
  number -= 1

number = 1

while number < 6:
  print(number)
  number += 1

num = 0
while True:
  print("Wprowadz liczbe lub exit aby zakonczyc")
  strData = input()
  if strData == 'exit': break
  num += int(strData)
  print("Wartosc po dodaniu liczby:", num)

number = 3

while number > 0:
  print(number) 
  number -= 1
else:
  print("Number po petli", number)
