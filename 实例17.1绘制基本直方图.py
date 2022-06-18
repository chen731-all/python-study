import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = rcParams["font.sans-serif"] = "SimHei"#设置中文支持，字体为黑体
ax = plt.figure().add_subplot()#建图，获取子对象ax
ax.bar(x = (0.2,0.6,0.8,1.2),height = (1,2,3,0.5),width = 0.1)
#有四根柱子，中心横坐标分别为      高度分别为           宽度为0.1
ax.set_title('我的直方图')
plt.show()
