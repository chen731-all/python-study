import numpy as np
import matplotlib.pyplot as plt
data = np.random.randint(0,100,30).reshape(5,6)
xlabels= ['beijing','shanghai',"chengdu",'guangzhou','hangzhou','wuhan']
ylabels= [2016,2017,2018,2019,2020]
ax = plt.figure(figsize=(10,8)).add_subplot()
ax.set_yticks(range(len(ylabels)))      #y轴在坐len（label）上加刻度
ax.set_yticklabels(ylabels)
ax.set_xticks(range(len(xlabels)))
ax.set_xticklabels(xlabels)
heatMp = ax.imshow(data,cmap=plt.cm.hot,aspect='auto',vmin=0,vmax=100)
for i in range(len(xlabels)):
    for j in range(len(ylabels)):
        ax.text(i,j,data[j][i],ha="center",va="center",color= 'blue',size= 26)
plt.colorbar(heatMp)
plt.xticks(rotation=45,ha="right")
plt.title("sales volume(ton)")
plt.show()