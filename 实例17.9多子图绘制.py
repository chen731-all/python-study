import matplotlib.pyplot as plt
import math,random
from matplotlib import rcParams
rcParams['font.family']=rcParams['font.sans-serif']= "SimHei"
def drawradar(ax):
    pi = 3.1415926
    labels = ['EQ','IQ','人缘','魅力','财富','体力']     #6个属性名子
    attrnum = len(labels)                            #属性种类数
    data = [7,6,8,9,8,2]                            #6个属性值
    angles = [2*pi*i/attrnum for i in range(attrnum)]   #6个属性的角度(以弧度为单位)
    angles2 = [x*180/pi for x in angles]                #一角度为单位
    ax.set_ylim(0,10)                                  #半径坐标范围
    ax.set_thetagrids(angles2,labels,fontproperties='SimHie')#绘制6条半径和圈圈
    ax.fill(angles,data,facecolor='green',alpha=0.25)
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
def drawpie(ax):
    lbs=('A','B','C','D')
    sectors=[16,29.55,44.55,10]         #占比
    expl=[0,0.1,0,0]
    ax.pie(x=sectors,labels=lbs,explode=expl,autopct='%.2f',shadow=True,labeldistance=1.1,pctdistance=0.6,startangle=90)
    ax.set_title("pie sample")
fig = plt.figure(figsize= (8,8))
ax = fig.add_subplot(2,2,1)     #把窗口分成两行两列取第一个子图
drawpie(ax)
ax= fig.add_subplot(2,2,2,projection= "polar")
drawradar(ax)
ax = fig.add_subplot(2,1,2)#ax = fig.subplot2grid((2,2),(1,0),colspan=2)         #把下面两个合成一个
drawplt(ax)
plt.figtext(0.5,0.5,"subplot sample")
plt.show()
