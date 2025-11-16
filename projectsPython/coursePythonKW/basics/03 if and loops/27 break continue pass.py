data = [2, 3, 1, 2, 1, 56, 21]

for i in data:
  if i == 3:
    break
  print(i*2)

print("")

for i in data:
  if i == 3 or i == 56:
    continue
  print(i*2)

if 1 > 2:
  pass
else:
  pass