def addNumbers(a,b,c):
  return a + b + c

def sumListElements(listData):
  if len(listData) == 0:
    print("Pusta lista")
    return None
  result = 0
  for element in listData:
    result += element
  return result

print(sumListElements([])) # None
print(sumListElements([1,2,3,4,5,6,7,8,9,10])) # 55

def printList(listData):
  if len(listData) == 0:
    return
  for element in listData:
    print(element)

printList([])
printList([6,7,8])