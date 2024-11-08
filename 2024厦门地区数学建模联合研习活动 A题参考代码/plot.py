import matplotlib.pyplot as plt
import numpy as np


def g(k):
	return - 0.5 * pow(k,2) + 3


def g0(k):
	return pow(k, 0)


x0 = np.linspace(1,2)
x = np.linspace(2,4)
y0 = g0(x0)
y = g(x)

plt.xlabel("k")
plt.ylabel("w")
plt.plot(x0, y0)
plt.plot(x, y)
plt.show()

