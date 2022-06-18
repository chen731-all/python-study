import matplotlib.pyplot as plt
ax = plt.figure().add_subplot()
labels = ["Jan","Fen","Mar","Apr"]
num1 = [20,30,15,35]
num2 = [15,30,40,20]
cordx = range(len(num1))
rect1 = ax.bar(x = cordx, height = num1, width = 0.5, color = 'red', label = 'Dept1')
rect2 = ax.bar(x = cordx, height = num2, width = 0.5, color = 'green',label= 'Dept2', bottom = num1)
ax.set_ylim(0, 100)         #y坐标范围
ax.set_ylabel("profit")     #y轴的含义
ax.set_xticks(cordx)        #x轴刻度位置
ax.set_xticklabels(labels)  #x轴刻度下的文字
ax.set_xlabel("In years 2021")
ax.set_title("MyCompany")
ax.legend()                    #在右上角显示图例说明
plt.show()

