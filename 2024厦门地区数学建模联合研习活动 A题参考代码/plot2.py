import matplotlib.pyplot as plt
import numpy as np


def p(s):
	return 0.4 * s



x = np.linspace(18,40)
y = p(x)

plt.xlabel("S")
plt.ylabel("w")
plt.plot(x, y)
plt.show()

