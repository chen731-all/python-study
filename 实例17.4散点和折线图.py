import math,random
import matplotlib.pyplot as plt
def drawplt(ax):
    xs = [i/100 for i in range(1500)]       #1500个横坐标，间隔0，01
    ys = [10*math.sin(x) for x in xs ]      #对应y轴坐标
    ax.plot(xs,ys,'red',label = 'Beijing')  #绘制曲线
    ys = list(range(-18,18))
    random.shuffle(ys)
    ax.scatter(range(16),ys[:16],c='blue') #画散点图
    ax.plot(range(16),ys[:16],'blue',label = "shanghai")#画折线图
    ax.legend()
    ax.set_xticks(range(16))
    ax.set_xticklabels(range(16))
ax=plt.figure(figsize=(10,4),dpi=100).add_subplot()
drawplt(ax)
plt.show()