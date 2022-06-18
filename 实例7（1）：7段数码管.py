import turtle as T
def drawline(draw):
    T.pendown() if draw else T.penup()
    T.fd(40)
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
    for i in date:
        drawdigit(eval(i))
def main():
    T.setup(800,350,200,200)
    T.penup()
    T.fd(-300)
    T.pensize(5)
    drawdate("20181010")
    T.hidetuitle()
    T.done()
main()
    
