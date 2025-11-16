# Zadanie: Kalkulator wieku psa na ludzkie lata
#
# Cel: Napisz program, który przeliczy wiek psa na ludzkie lata.

# Kroki do wykonania:
# 1. Poproś użytkownika o wprowadzenie wieku psa w latach i zapisz tę wartość do zmiennej.
# 2. Użyj instrukcji warunkowych, aby obliczyć wiek psa w ludzkich latach. 
#    - Pierwszy rok życia psa to 15 ludzkich lat. human_age = dog_age * 15
#    - Drugi rok życia psa to kolejne 9 ludzkich lat. human_age = 15 + (dog_age - 1) * 9
#    - Każdy kolejny rok to 5 ludzkich lat. 24 + (dog_age - 2) * 5
# 3. Jeśli podana wartość wieku psa jest mniejsza niż 0, wyświetl komunikat o błędzie.
# 4. Wyświetl wynik obliczeń w konsoli. 

wiekPsa = float(input("Podaj wiek psa: "))

if wiekPsa >= 2:
  ludzkieLata = 24 + (wiekPsa - 2) * 5 
  print("Wiek psa na ludzkie wynosi: ", ludzkieLata)
elif wiekPsa > 1:
  ludzkieLata = 15 + (wiekPsa - 1) * 9
  print("Wiek psa na ludzkie wynosi: ", ludzkieLata)
elif wiekPsa > 0:
  ludzkieLata = 15 * wiekPsa
  print("Wiek psa na ludzkie wynosi: ", ludzkieLata)
else:
  print("Podano bledna wartosc.")




