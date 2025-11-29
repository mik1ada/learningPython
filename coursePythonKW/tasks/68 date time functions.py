import time
import datetime
import random

startTime = datetime.datetime.now()
print('Czas rozpoczecia zadania:', startTime.strftime("%H:%M:%S"))

sleepTime = random.randint(1,5)
time.sleep((sleepTime))

endTime = datetime.datetime.now()
print('Czas zakonczenia zadania:', endTime.strftime("%H:%M:%S"))

workTime = endTime - startTime
print("Czas pracy:", workTime)

if workTime.total_seconds() > 3:
  print("Duzo wlozonego czasu w projekt")
else:
  print("Krotki czas pracy wlozony w projekt")