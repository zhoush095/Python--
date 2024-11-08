import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["savefig.dpi"] = 1200
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

water = np.array([77.2 / 100, 22.4 / 100, 0.4 / 100])
plt.pie(water, labels=['冰川、冰盖', '地下水', '可供人类利用的水'], colors=["#d5695d", "#5d8ca8", "#65a479"],
        autopct='%.2f%%', textprops={'fontsize': 7})
plt.title("淡水资源分布扇形图")
plt.show()
