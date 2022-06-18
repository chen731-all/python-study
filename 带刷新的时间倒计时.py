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
    drawline(True) if digit in [2,3,4,5]else drawline(False)
    drawline(True) if digit in [1,3,4,5]else drawline(False)
    drawline(True) if digit in [2,3,5]else drawline(False)
    drawline(True) if digit in [2]else drawline(False)
    T.left(90)
    drawline(True) if digit in [4,5]else drawline(False)
    drawline(True) if digit in [2,3,5]else drawline(False)
    drawline(True) if digit in [1,2,3,4]else drawline(False)
    T.penup()
    T.fd(40)
    T.left(180)
def drawcishu(cishu):
    T.pencolor("red")
    for i in cishu:
        drawdigit(eval(i))
        t.sleep(1)
        T.clear()
def main():
    T.penup()
    T.fd(30)
    T.pensize(5)
    drawcishu("54321")
    T.done()
main()
