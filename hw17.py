from GPSPhoto import gpsphoto
import json
print (gpsphoto.getGPSData('C:/Users/User/20210210_175742.jpg'))
a = gpsphoto.getGPSData('C:/Users/User/20210210_175742.jpg')
s = str(a.get('Latitude'))+","+str(a.get('Longitude'))
print (s)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(s, f, ensure_ascii = False)