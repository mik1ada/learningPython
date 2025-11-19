# Stwórz funkcje do konwersji czasu:
# 1) convertToSeconds przyjmująca ilość godzin
#    oraz minut i zwracająca ilość sekund.
#    Jako parametry funkcji zapisz: hours, minutes.
#    Skonwertuj 3 godziny i 25 minut na sekundy,
#    wynik pokaż w konsoli.
# 2) convertToHours przyjmującą parametr minutes
#    oraz zwracając ilość godzin.
#    Skonwertuj 120 minut na godziny i pokaż
#    wynik w konsoli.

def convertToSeconds(hours, minutes):
  minutes += hours * 60
  seconds = minutes * 60
  return seconds

def convertToHours(minutes):
  hours = minutes / 60
  return hours

print(convertToSeconds(3,25))
print(convertToHours(120))