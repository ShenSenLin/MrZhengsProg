"""
将生成的地形图形化输出
问万林，视具体情况定
"""


import matplotlib.pyplot as plot

y = [42, 43, 43, 50, 75, 50, 44, 12, 26, 32]
x = [i for i in range(len(y))]

fig, ax = plot.subplots(figsize=(12, 4))
ax.plot(x, y, label='y', color='red')
ax.set_title('Terrain Show')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
# plt.savefig('line_plot.png')
plot.show()
