import time
import datetime

ticks = time.time()
print(ticks)

timeData = time.localtime()
print(timeData)
print(timeData.tm_year)

timeData = time.localtime(10)
print(timeData)
print(timeData.tm_year)

result = time.asctime(time.localtime())
print(result)

timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S", timeData))

timeStr = "17:23:45 09.12.2025"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)

i = 0
while i < 3:
  time.sleep(1)
  i += 1
  print(time.asctime(time.localtime()))

tStart = time.perf_counter()
time.sleep(1.1)
tEnd = time.perf_counter()

result = tEnd - tStart

print("Code took:", result, "seconds")

dateTimeObject = datetime.datetime.now()
print(dateTimeObject)
# print(dir(dateTimeObject))

dateTimeObject = datetime.datetime(2025, 11, 29)
dateTimeObject = datetime.datetime(2025, 11, 29, 19, 7, 20)
print("date(): ", dateTimeObject.date())
print("time(): ", dateTimeObject.time())
print("timestamp(): ", dateTimeObject.timestamp())
print("today(): ", dateTimeObject.today())
print("year: ", dateTimeObject.year)
print("month: ", dateTimeObject.month)
print("day: ", dateTimeObject.day)
print("hour: ", dateTimeObject.hour)
print("minute: ", dateTimeObject.minute)
print("second: ", dateTimeObject.second)

print("format: ", dateTimeObject.strftime("%H:%M:%S, %d.%m.%Y"))

dateTimeObject = dateTimeObject.now()
print("format: ", dateTimeObject.strftime("%H:%M:%S, %d.%m.%Y"))

datetime1 = datetime.datetime(2025, 1, 1, 23, 59, 59)
datetime2 = datetime.datetime(2030, 1, 1, 23, 59, 59)

print(datetime2 > datetime1)
print(datetime2 < datetime1)

date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2027, 1, 1)

print(date2 > date1)
print(date2 < date1)