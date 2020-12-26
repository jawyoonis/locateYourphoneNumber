import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
#from .carrierdata import CARRIER_DATA, CARRIER_LONGEST_PREFI


phone_number1= phonenumbers.parse('+14845029957')
print(phone_number1)
print(geocoder.description_for_number(phone_number1, "en"))
print(carrier.name_for_number(phone_number1, "en"))
phone_number2= phonenumbers.parse('+252634118328')
print(phone_number2)
print(geocoder.description_for_number(phone_number2, "en"))
print(carrier.name_for_number(phone_number2, "en"))
