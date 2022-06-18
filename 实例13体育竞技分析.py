import random as R
def printintro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（0-1之间小数表示）")


def getinputs():
    a = eval(input("请输入选手A的能力值（0-1）："))
    b = eval(input("请输入选手B的能力值（0-1）："))
    n = eval(input("模拟比赛的场次"))
    return a,b,n

def printsummerary(winsA,winsB):
    n = winsA + winsB
    print("竞技分析开始一共{}场比赛".format(n))
    print("选手A赢了{}场比赛，获胜占比{:0.1%}".format(winsA,winsA/n))
    print("选手B赢了{}场比赛，获胜占比{:0.1%}".format(winsB,winsB/n))

def gameover(a,b):
    return a==15 or b==15

def yici(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameover(scoreA,scoreB):
        if serving =="A":
            if R.random() < probA:
                scoreA+=1
            else:
                serving="B"
        else:
            if R.random() < probB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB

def guocheng(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = yici(probA,probB)
        if scoreA > scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB

def main():
    printintro()
    probA,proB,n = getinputs()
    winsA,winsB = guocheng(n,probA,proB)
    printsummerary(winsA,winsB)

main()
