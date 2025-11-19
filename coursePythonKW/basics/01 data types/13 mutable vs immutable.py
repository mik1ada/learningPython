# immutable types: int, float, bool, str, tuple, frozenset

a = 1
addr1 = id(a)
a += 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)  # False

# mutable types: list, dict, set

b = [1, 2, 3]
addr3 = id(b)
b.append(4)
addr4 = id(b)

print(addr3)
print(addr4)
print(addr3 == addr4)  # True