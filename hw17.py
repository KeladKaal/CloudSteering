from GPSPhoto import gpsphoto
import pickle
print (gpsphoto.getGPSData('C:/Users/User/20210210_175742.jpg'))
a = gpsphoto.getGPSData('C:/Users/User/20210210_175742.jpg')
s = str(a.get('Latitude'))+","+str(a.get('Longitude'))
print (s)

output = open('data.pkl', 'wb')
pickle.dump(s, output, 2)
output.close()