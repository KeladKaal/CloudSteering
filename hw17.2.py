from geopy.geocoders import Nominatim
import json
input = open('data.pkl', 'rb')
my_cool_f = open("data.json")
s = json.load(my_cool_f)
my_cool_f.close()
geolocator = Nominatim(user_agent="migulaevat@gmail.com")
location = geolocator.reverse(s)
print('location: ', location.address)
print('Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=',s,sep="")