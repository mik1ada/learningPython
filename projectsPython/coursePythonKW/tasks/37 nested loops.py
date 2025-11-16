# Zadanie: Wypisanie elementów z listy list
#
# Cel: Napisz program, który przechodzi przez zagnieżdżoną listę (listę list)
# i wypisuje wszystkie jej elementy. 
#
# Kroki do wykonania:
# 1) Stwórz zmienną 'nested_list', która będzie zawierać kilka list z różnymi typami elementów.
# 2) Użyj zagnieżdżonej pętli for do przejścia przez wszystkie listy i ich elementy.
# 3) Wypisz każdy element z każdej listy.

nestedList = [
  [0,1,2,3,4],
  ["Ola", "Ala", "Adam"],
  [10, "Adam", 20, "Ania"]
]

for list in nestedList:
  for element in list:
    print(element)