from geopy.geocoders import Nominatim
import pickle
input = open('data.pkl', 'rb')
s = pickle.load(input)
geolocator = Nominatim(user_agent="migulaevat@gmail.com")
location = geolocator.reverse(s)
print('location: ', location.address)
print('Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=',s,sep="")