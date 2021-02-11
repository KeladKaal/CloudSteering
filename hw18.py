import os
from PIL import Image

img = Image.open('C:/Users/User/20210210_175742.jpg')
width,height = 800,600
if img.size[0] < img.size[1]:
    width,height = height,width

resized_img = img.resize((width, height), Image.ANTIALIAS)
resized_img.save('photo-resized.jpg')
a = os.path.getsize("C:/Users/User/20210210_175742.jpg")
print('size before ',a)
b = os.path.getsize("photo-resized.jpg")
print('size after', b)