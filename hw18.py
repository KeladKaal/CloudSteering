import os
from PIL import Image

print ("Write your photo address like: C:/Users/User/20210210_175742.jpg")

s = input()
img = Image.open(s)
width,height = 800,600
if img.size[0] < img.size[1]:
    width,height = height,width

resized_img = img.resize((width, height), Image.ANTIALIAS)
resized_img.save('photo-resized.jpg')
a = os.path.getsize(s)
print('size before ',a)
b = os.path.getsize("photo-resized.jpg")
print('size after', b)