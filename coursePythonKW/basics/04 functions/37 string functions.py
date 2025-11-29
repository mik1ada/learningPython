print("Hello " + "world!")
print("Hello"*3)

string = "Hello World!"
print(string[0]) # H
print(string[0:5]) # Hello

print("Hello" in string) # True
print("Hello" not in string) # False

multiline = """line 1
line 2
line 3"""
print(multiline)

print('ala'.capitalize())
print("Ola ma kota, Ola ma psa".count('Ola'))

print("Hello World".center(20, " "))
print(string.startswith("Hello")) 
print(string.endswith("World!"))

print(string.find('Ola')) # -1
print(string.find('H')) # 0
print("Ola ma kota, Ola ma psa".rfind("Ola")) # 13

print("2341232".isalnum()) # True
print("234123.2".isalnum()) # False
print("abcdefghijkl".isalpha()) # True

print("test".islower()) # True
print("TeST".isupper()) # False
print("  \n\t".isspace()) # True

print("-|".join(['Ala','Ola','Kot']))
print("Hello World".lower())
print("Hello World".swapcase())

print("     \n Hello World \n\n\n\n\n".lstrip())

print("Ala ma trzy psy, Ala ma trzy koty".replace("Ala","ZBIGNIEW"))
print("My name is {myName}, I'm from {country}".format(myName = 'Mikolaj', country = 'Poland'))