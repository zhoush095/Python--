import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["savefig.dpi"] = 1200
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

water = np.array([96.53 / 100, 2.53 / 100, 0.94 / 100])
plt.pie(water, labels=['海洋水', '淡水', '其他'], colors=["#d5695d", "#5d8ca8", "#65a479"], autopct='%.2f%%',
        textprops={'fontsize': 7})
plt.title("世界水资源分布扇形图")
plt.show()
