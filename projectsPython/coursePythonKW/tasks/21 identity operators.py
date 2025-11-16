text = 'Hello'
print(text.upper())

print(dir(text))

x = 256
y = 256

print(x is y)

listOne = [1, 'Słoń', 25.0]
listTwo = listOne

print(listOne is listTwo)

listOne.append('Źrebie')

if listOne is listTwo:
  print("Listy po dodaniu elementu nadal są tą samą listą")
  print(listTwo)

listThree = [1, 'Słoń', 25.0, 'Źrebie']

if listOne is listThree:
  print("Lista pierwsza i trzecia są tą samą listą")
else:
  print("To dwie różne listy")