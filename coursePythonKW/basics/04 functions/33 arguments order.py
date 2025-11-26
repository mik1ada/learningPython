def printCar(brand, / , name = "concept", * , year = 1960, color = "black"):
  print(brand, name, year, color)

printCar("Ford", color = 'red', year = 1973)
printCar("Ford", name = 'Mustang', color = 'red', year = 1973)