# 1. Stwórz set z unikalnymi wartościami jak:
#    Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2. Dodaj do set za pomocą funkcji add kolejne elementy:
#    Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaż w konsoli wielkość set
# 4. Wykorzystaj pętlę for aby pokazać elementy w set

imiona = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}

imiona.update(["Olek", "Basia", "Kasia", "Karol", "Zuza", "Paulina"])

print("Wielkość set:", len(imiona))

for imie in imiona:
  print(imie)