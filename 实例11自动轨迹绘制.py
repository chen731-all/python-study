import turtle as T
T.title("自动轨迹绘制")
T.setup(800,600,0,0)
T.pencolor("red")
T.pensize(5)
#数据读取
d = []
f = open("date.txt")
for line in f:
    line = line.replace("\n", "")
    d.append(list(map(eval,line.split(","))))
f.close()
#自动绘制
for i in range(len(d)):
    T.pencolor(d[i][3],d[i][4],d[i][5])
    T.fd(d[i][0])
    if d[i][1]:
        T.right(d[i][2])
    else :
        T.left(d[i][2])