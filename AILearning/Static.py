#coding:utf-8
from numpy import *
from matplotlib import pyplot
import scipy.stats.stats as st
from scipy import *
from scipy.stats import norm
from scipy.integrate import trapz

x_norm = norm.rvs(size=500)
h = pyplot.hist(x_norm)
#
x = linspace(-3, 3, 50)
x1 = linspace(-2, 2, 108)
p = trapz(norm.pdf(x1), x1)
print(p)
print('{:.2%} of the value lie between -2 and 2'.format(p))
pyplot.fill_between(x1, norm.pdf(x1), color='red')
# pyplot.plot(x, norm.pdf(x), 'k-')
pyplot.title("Hist")
pyplot.show()