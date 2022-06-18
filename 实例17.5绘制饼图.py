import matplotlib.pyplot as plt
def drawpie(ax):
    lbs=('A','B','C','D')
    sectors=[16,29.55,44.55,10]         #占比
    expl=[0,0.1,0,0]
    ax.pie(x=sectors,labels=lbs,explode=expl,autopct='%.2f',shadow=True,labeldistance=1.1,pctdistance=0.6,startangle=90)
    ax.set_title("pie sample")
ax = plt.figure().add_subplot()
drawpie(ax)
plt.show()