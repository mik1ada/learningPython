setData = {2, 3, 1, 4, 5, 6, 2, 3, 4}
setData.add(7)

setData.discard(1)

print(type(setData))
print(setData)

for element in setData:
    print(element)

frozenData = frozenset([2, 3, 1, 4, 5, 6, 2, 3, 4])
# frozenData.add(7)  # This will raise an AttributeError
print(type(frozenData))  
print(frozenData)

