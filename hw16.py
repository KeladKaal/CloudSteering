from geopy.geocoders import Nominatim
s = input()
geolocator = Nominatim(user_agent="migulaevat@gmail.com")
location = geolocator.reverse(s)
print('location: ', location.address)
print('Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=',s,sep="")