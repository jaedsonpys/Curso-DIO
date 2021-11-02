import phonenumbers
from phonenumbers import geocoder

number = str(input('Digite um número de telefone (Ex: +558299887766): '))
phone_number = phonenumbers.parse(number)

# Obtendo o local do número de telefone
geolocation = geocoder.description_for_number(phone_number, 'pt')
print(geolocation)