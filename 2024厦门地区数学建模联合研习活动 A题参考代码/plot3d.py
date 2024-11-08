import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")
s = np.arange(18, 22, 1 / 100)
k = np.arange(1, 3, 1 / 100)
m = 0
p = []


def g(x):
    if 1 <= x <= 1.5:
        return 1
    else:
        return 2.25 - np.pow(x, 2)


for s1 in s:
    y1 = (2 * np.floor(34 / np.sqrt(s1 / k)) - 2 + 3 * np.floor((25 - k * np.sqrt(s1 / k)) / np.sqrt(s1 / k))) / 5
    w1 = [g(i) * 0.5 + 0.4 * s1 for i in k]
    w1 = np.array(w1)
    y1 += w1
    k0 = 0
    for i in y1:
        k0 += 1
        if i > m:
            m = i
            p = [m, k[k0], s1]
    ax.plot(y1 * 0.65, k, s1)
print(p)
plt.xlabel("用户舒适度")
plt.ylabel("长宽比例")
# ax.legend()
plt.show()