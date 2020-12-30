import phonenumbers as phonenumbers
from phonenumbers import carrier
number = str(input('enterbthe phone number: '))
phone_number = phonenumbers.parse(number)

print(carrier.name_for_number(phone_number, 't'))
	