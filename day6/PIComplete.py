# coding:UTF-8

from random import random
from math import sqrt
from time import clock

DARTS = 120000000
hits = 0
clock()

for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * ((hits*1.0)/DARTS)

print('PI的值是%s' % pi)

print((4.0/5))

print('程序运行的时间是 %-5ss' % clock())