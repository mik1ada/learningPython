contacts = {
  "Marek": 456789123,
  "Anna": 123456789,
  "Janek": "mail.janka@domena.com"
}

contacts["Rafał"] = "rafal@example.com"

print(contacts["Janek"])
print(type(contacts))
print(len(contacts))

print(contacts.keys())
print(contacts.values())

for key in contacts:
  print(key + " " + str(contacts[key]))

for key, value in contacts.items():
  print(f"{key}: {value}")