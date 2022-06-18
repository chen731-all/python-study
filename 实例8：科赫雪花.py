import turtle as T
def koch(size,n):
    if n==0:
        T.fd(size)
    else:
        for angle in [0,60,-120,60]:
            T.left(angle)
            koch(size/3,n-1)
def main():
    T.setup(600,600)
    T.penup()
    T.goto(-200,100)
    T.pendown()
    T.pensize(2)
    T.colormode(255)
    T.color(0,255,0)
    level =3
    koch(400,level)
    T.right(120)
    koch(400,level)
    T.right(120)
    koch(400,level)
    T.hideturtle()
main()

    
    
