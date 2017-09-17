# coding:utf=8

import urllib2
#少奇
response = urllib2.urlopen("http://placekitten.com/g/500/600")
cat_img = response.read()

print(response.getcode())

print(response.geturl())

print(response.info())

with open("car_500_600.jpg", "wb") as f:
    f.write(cat_img)
