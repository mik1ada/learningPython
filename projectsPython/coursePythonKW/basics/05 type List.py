lista = ["Rafał", 7, 'Adam', 150.1]
print(lista)
print(type(lista))
print( lista[0] )
print( lista[1] )
print( lista[-1] )
print ( len(lista) )
print (lista[0:2])


data = ['Ola', 'Rafał', 23, 45, 'Daniel']
print( len(data) ) 

data[2] = 'Paweł'
data[3] = 'Ania' 

del data[1] 
print(data)

print( 45 in data )
print ( 100 in data ) 

if 'Olaxx' in data:
    print('Ola jest w liście data')

for v in range (len(data)):
    if ( len(data[v]) <=3 ): 
        print(data[v])


for v in data:
    print(v)