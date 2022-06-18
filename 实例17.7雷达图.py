import matplotlib.pyplot as plt
from matplotlib import rcParams
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
rcParams['font.family'] = rcParams["font.sans-serif"] = "SimHei"
ax = plt.figure().add_subplot(projection='polar')
drawradar(ax)
plt.show()

