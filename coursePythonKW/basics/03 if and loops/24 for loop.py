for v in [1, 2, 3, 4]:
  print(v * 2)

for v in ("Ania", "Ola", "Rafal"):
  print(v)

for el in {3, 4, 5, 6, "Ola"}:
  print(el)

for v in "Hello":
  print(v)
else:
  print("Petla zakonczona")

dictionaryData = {
  "Ania": "ania@example.com",
  "Adam": "adam@gmail.com"
}

for key in dictionaryData:
  print(key)

for key in dictionaryData:
  print(dictionaryData[key])

for key, value in dictionaryData.items():
  print(key, " : ", value)

for v in dictionaryData.values():
  print(v)