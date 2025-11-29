import math
import random

print(type(str(13)))
print(type(str([37, 13])))

number = int("1233")
print(type(number))

number += 11
print(number)

floatNum = float("45.12")
print(type(floatNum))
floatNum = floatNum * 3
print(floatNum)


print(abs(-7))
print(abs(7))

print(math.ceil(13.21))
print(math.floor(13.21))

print(max(10, 1, -90))
print(min(-23, 0, 123))

print(4 ** 3) # 64
print(pow(4,3)) # 64

print(math.sqrt(128))

print(round(12.7892341, 2))

print(random.random())

print(random.choice([0,12,24,36,48]))
print(random.choice(('Zbigniew','Stefan','Marek')))

print(random.randrange(-10, 25, 5))

listData = [0,2,4,6,8,10,12]
random.shuffle(listData)
print(listData)