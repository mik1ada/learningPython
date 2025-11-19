numbers = list(range(-4,5))

for number in numbers:
  if number == 0:
    print("0 jest parzyste")
  elif number % 2 == 0:
    print(number, "jest parzysta")
  else:
    print(number, "jest nieparzysta")