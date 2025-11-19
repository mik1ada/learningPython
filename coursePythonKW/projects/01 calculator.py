num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
  if reset == True:
    num = float(input("Podaj pierwsza cyfre:"))
    reset = False
  
  operation = input("Podaj znak dzialania operacji arytmetycznej do wyboru" + str(calcOperations) + "lub exit jesli chcesz zakonczyc lub reset: ")
  if operation == 'exit': break
  if operation == 'reset':
    reset = True
    continue

  if not operation in calcOperations:
    print("Wprowadzona zostala bledna operacja.")
    continue
  
  secondNum = float(input("Podaj druga liczbe:"))

  if operation == "+":
    result = num + secondNum
  elif operation == "-":
    result = num - secondNum
  elif operation == "*":
    result = num * secondNum
  elif operation == "/":
    result = num / secondNum
  else: 
    result = num ** secondNum

  print("Wynik operacji: ", str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))
  num = result
  result = None