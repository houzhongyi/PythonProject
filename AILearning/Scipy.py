import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True)
data = np.genfromtxt("JANAF_CH4.txt",
                     delimiter="\t",
                     skip_header=1,
                     names=True,
                     missing_values="INFINITE",
                     filling_values=np.inf)
for row in data[:7]:
    print("{}\t{}".format(row['TK'], row['Cp']))
print("...\t...")
p = plt.plot(data['TK'], data['Cp'], 'kx')
t = plt.title("JANAF data for Methane $CH_4$")
a = plt.axis([0, 6000, 30, 120])
x = plt.xlabel("Temperature (K)")
y = plt.ylabel(r"$C_p$ ($\frac{kJ}{kg K}$)")
plt.show()

