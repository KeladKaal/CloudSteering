from geopy.geocoders import Nominatim
print("Write your coordinates like: 60.016666666666666,30.322")
s = input()
geolocator = Nominatim(user_agent="migulaevat@gmail.com")
location = geolocator.reverse(s)
print('location: ', location.address)
print('Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=',s,sep="")