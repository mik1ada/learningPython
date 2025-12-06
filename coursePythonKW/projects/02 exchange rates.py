import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/a/?format=json")

if response.ok == True:
  data = response.json()
  date = data[0]['effectiveDate']
  rates = data[0]['rates']

print("Data publikacji:", date)
for rate in rates:
  print(rate['code'], "=", rate['mid'], "PLN")