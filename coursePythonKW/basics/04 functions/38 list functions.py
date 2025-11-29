list1 = [0,2,4,6,8]

print(list1[3])
print(list1[2:4])

list1[0] = 9
print(list1)

del list1[1]
print(list1)

print(len(list1))
print(max(list1))
print(min(list1))

print(list(('Ala','Basia')))

print([0,2,4] + [1,3,5])
print([0,1]*3)

print(9 in [0,2])
print(9 not in [0,2])

list1.append(99)
print(list1)

print(list1.count(3))
list1.append(3)
print(list1.count(3))

list1.extend([12,14,16])
print(list1)

list1.insert(0, 10000)
print(list1)

print(list1.index(12)) # 7

list1.reverse()
print(list1)

list1.sort()
print(list1)

num = list1.pop(2)
print(num)
print(list1)