data = ("Ala", "Ola", "Kasia")

# data[0] = "Rafał" # Błąd! Krotki są niemodyfikowalne (immutable)

names = data + ("Rafał",)  
print(names)  
print(len(names))
print(type(names))

numbers = 1, 2, 3,
print(type(numbers))

emptyTuple = ()
print(emptyTuple)
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:3]) 

cars = ( ("Dodge", "Ford"), ("Pontiac", "Chevrolet") )
print(cars[0][0]) # Dodge

if "Ford" in cars[0]:
  print("Ford jest w krotce nr. 1")

del cars
# print(cars)  # Błąd! Krotka została usunięta

# del names[0] # Błąd! Krotki są niemodyfikowalne (immutable)

tupleX3 = names * 3
print(tupleX3)
print(type(tupleX3))