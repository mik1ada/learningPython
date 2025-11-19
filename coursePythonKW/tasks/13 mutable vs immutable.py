# Zadanie do wykonania:
# 1. Zadeklaruj zmienną 'number' z int o wartości 5 i wyświetl jej adres w pamięci.
# 2. Zwiększ wartość zmiennej 'number' o 2 i ponownie wyświetl jej adres w pamięci. 
# 3. Utwórz listę 'fruits' z trzema owocami: "apple", "banana", "cherry".
#    Wyświetl adres w pamięci listy.
# 4. Dodaj do listy 'fruits' kolejny owoc: "orange" i wyświetl adres w pamięci listy. 
# 5. Na podstawie wykonanych czynności wyjaśnij różnicę między typami mutowalnymi
#    a niemutowalnymi.

number = 5
print("Adres w pamieci:", id(number))

number += 2
print("Adres w pamieci po dodaniu 2:", id(number))

fruits = ["apple", "banana", "cherry"]
print("Adres w pamieci listy fruits:", id(fruits))

fruits.append("orange")
print("Adres w pamieci listy fruits po dodaniu 'orange':", id(fruits))

# Wyjaśnienie:
# Typy niemutowalne (immutable), takie jak int, tworzą nowy obiekt w pamięci
# przy każdej zmianie wartości, co skutkuje różnymi adresami w pamięci.
# Typy mutowalne (mutable), takie jak list, zachowują ten sam obiekt 
# w pamięci nawet po modyfikacji jego zawartości, więc adres pozostaje taki sam.


