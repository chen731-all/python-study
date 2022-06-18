import turtle as T
import time as t
def drawgap():
    T.penup()
    T.fd(5)
def drawline(draw):
    drawgap()
    T.pendown() if draw else T.penup()
    T.fd(40)
    drawgap()
    T.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    T.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    T.left(180)
    T.penup()
    T.fd(20)
def drawdate(date):
    T.pencolor("red")
    for i in date:
        if i == "-":
            T.write("年",font=("Arial",18,"normal"))
            T.pencolor("green")
            T.fd(40)
        elif i == "=":
            T.write("月",font=("Arial",18,"normal"))
            T.pencolor("blue")
            T.fd(40)
        elif i=="+":
            T.write("日 ",font=("Arial",18,"normal"))
            T.pencolor("yellow")
            T.fd(40)
        elif i=="*":
             T.write("时",font=("Arial",18,"normal"))
             T.fd(40)
        elif i=="/":
             T.write("分",font=("Arial",18,"normal"))
             T.fd(40)
        elif i=="_":
             T.write("秒",font=("Arial",18,"normal"))
             T.fd(40)
        else:
            drawdigit(eval(i))
def main():
    T.setup(1600,700,10,50)
    T.penup()
    T.fd(-300)
    T.pensize(5)
    drawdate(t.strftime("%y-%m=%d+%H*%M/%S_",t.localtime(t.time()) ))
    T.hideturtle()
    T.done()
main()
    
