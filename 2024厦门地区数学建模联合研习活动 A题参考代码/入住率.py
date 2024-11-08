import numpy as np

w = np.array([5.95, 6.514, 15.78 * 0.4])
d = np.interp(w, (w.min(), w.max()), (0.5, 0.75))
print(d)
