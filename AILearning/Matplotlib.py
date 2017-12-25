import pylab as pl
from numpy import *
#y = x*x
# x = range(10)
# y = [i*i for i in x]
# pl.plot(x,y)
#y = sin(x)
# x = linspace(0, 2*pi, 50)
# pl.scatter(x, sin(x))
#scatter
# x = random.rand(200)
# y = random.rand(200)
# size = random.rand(200) * 80
# color = random.rand(200)
# pl.scatter(x, y, size, color)
#many figure
t = pl.linspace(0, 2*pi, 50)
x = sin(t)
y = cos(t)
pl.figure(x)
pl.plot(x)
pl.figure(y)
pl.plot(y)
pl.subplot(1, 2, 1)
pl.plot(x)
pl.subplot(1, 2, 2)
pl.plot(y)
pl.show()