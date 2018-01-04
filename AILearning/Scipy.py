#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate.rbf import Rbf
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(precision=2, suppress=True)
data = np.genfromtxt("JANAF_CH4.txt",
                     delimiter="\t",
                     skip_header=1,
                     names=True,
                     missing_values="INFINITE",
                     filling_values=np.inf)
# for row in data[:7]:
#     print("{}\t{}".format(row['TK'], row['Cp']))
# print("...\t...")
# p = plt.plot(data['TK'], data['Cp'], 'kx')
# t = plt.title("JANAF data for Methane $CH_4$")
# a = plt.axis([0, 6000, 30, 120])
# x = plt.xlabel("Temperature (K)")
# y = plt.ylabel(r"$C_p$ ($\frac{kJ}{kg K}$)")
# plt.show()
# ch4_cp = interp1d(data['TK'], data['Cp'],
#                   bounds_error=False, fill_value=-999.25)
# print(ch4_cp(382.2))
# print(ch4_cp([32.2,323.2]))
# print(ch4_cp(8752))
# T = np.arange(100, 355, 5)
# plt.plot(T, ch4_cp(T), "+k")
# p = plt.plot(data['TK'][1:7], data['Cp'][1:7], 'ro')
# cp_ch4 = interp1d(data['TK'], data['Cp'], kind="nearest")
# p = plt.plot(T, cp_ch4(T), "k^")
# p = plt.plot(data['TK'][1:7], data['Cp'][1:7], 'ro', markersize=8)
# cp_rbf = Rbf(data['TK'], data['Cp'], function="inverse_multiquadric")
# plt.plot(data['TK'], data['Cp'], 'k+')
# p = plt.plot(data['TK'], cp_rbf(data['TK']), 'r-')
#三维数据点
x, y = np.mgrid[-np.pi/2:np.pi/2:5j, -np.pi/2:np.pi/2:5j]
z = np.cos(np.sqrt(x**2 + y**2))
# fig = plt.figure(figsize=(12, 6))
# ax = fig.gca(projection="3d")
# ax.scatter(x, y, z)
#三维RBF插值
zz = Rbf(x, y, z)
xx, yy = np.mgrid[-np.pi/2:np.pi/2:100j, -np.pi/2:np.pi/2:100j]
fig = plt.figure(figsize=(12, 6))
ax = fig.gca(projection="3d")
ax.scatter(x, y, z)
ax.plot_surface(xx, yy, zz(xx, yy), rstride=1, cstride=1, cmap=plt.cm.jet)
plt.show()