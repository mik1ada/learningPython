listData = [1, 2, 3, 4, 5, 6]
tupleData = tuple(listData)

print(tupleData)

otherList = list(("Ola", 23, 234))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

frozensetData = frozenset(listData)
print(type(frozensetData))
print(frozensetData)

tupleData = ( ("Ola", 2312), ("Kasia", 3423), ("Adam", 1234) )

dictData = dict(tupleData)
print(dictData)