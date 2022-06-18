import matplotlib.pyplot as plt
ax = plt.figure(figsize=(10,5)).add_subplot()
ax.set_ylim(0,400)
ax.set_xlim(0,80)
x1 = [7,17,27,37,47,57]
x2 =[13,23,33,43,53,63]
x3 =[10,20,30,40,50,60]
y1 = [41,39,13,69,39,14]
y2 = [123,15,20,105,79,37]
y3 = [124,91,204,264,221,175]
rects1 = ax.bar(x1,y1,facecolor='red',width=3,label="ipone")
rects2 = ax.bar(x2,y2,facecolor= 'green',width=3,label="huawei")
rects3 = ax.bar(x3,y3,facecolor='blue',width=3,label="xioami")
ax.set_xticks(x3)
ax.set_xticklabels(('A1','A2','A3','A4','A5','A6'))
ax.legend()
def label(ax,rects):                                #在每个主子顶端标注柱子的值
    for rect in rects:
        height = rect.get_height()                  #柱子的高度
        ax.text(rect.get_x()+rect.get_width()/2,height+14,str(height),rotation=90)#旋转90度
label(ax,rects1)
label(ax,rects2)
label(ax,rects3)
plt.show()