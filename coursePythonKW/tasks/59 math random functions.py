import math
import random

distance = random.randint(100, 1000)
expectedFuleUsage = math.ceil((distance / 100) * 7)

fuelPrice = round(random.uniform(4.5, 5.5), 2)

totalCost = fuelPrice * expectedFuleUsage
print(totalCost)

if totalCost > 400:
  print("Costs of travel are too high")
else:
  print("This is good price, let's go!")