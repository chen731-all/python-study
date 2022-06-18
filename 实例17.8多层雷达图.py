import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']=rcParams['font.sans-serif']= "SimHei"
pi = 3.1415926
label=["EQ","IQ","人缘","魅力","财富","体力"]
attrnum=len(label)
name = ["张三","李四","王五"]
data = [[0.4,0.32,0.35],[0.85,0.35,0.30],[0.40,0.32,0.35],[0.40,0.82,0.75],[0.14,0.12,0.35],[0.8,0.92,0.35]]
angles=[2*pi*i/attrnum for i in range(attrnum)]
angles2=[x*180/pi for x in angles]
ax = plt.figure().add_subplot(projection = "polar")
ax.fill(angles,data,alpha=0.25)
ax.set_thetagrids(angles2,label)
ax.set_title("三人人格分析",y=1.05)
ax.legend(name,loc=(0.95,0.9))
plt.show()