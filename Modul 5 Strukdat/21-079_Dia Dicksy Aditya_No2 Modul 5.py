import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen
turtle.speed = (10)


def Squre(level, dis):
    color = ["white", "white", "white", "white"]
    id = level % 4

    if level == 0:
        print()
        print("outter")
        my_turtle.begin_fill()
        my_turtle.color("black", color[id])
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)

        #inline
        print("inline2")
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)

        #inline2
        print("inline2")
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.end_fill()

        Squre(level - 1, dis / 2)
    else:
        #outer
        print
        print("Outer")
        my_turtle.begin_fill()
        my_turtle.color("black", color[id])
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)

        #inline1
        print("inline1")
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)

        #inline2
        print("inline2")
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)

        #inline3
        print("inline3")
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.forward(dis * 2)
        my_turtle.right(90)
        my_turtle.forward(dis)
        my_turtle.right(90)
        my_turtle.end_fill()

        Squre(level - 1, dis / 2)


def main():
    my_turtle.penup()
    my_turtle.goto(-200, 200)
    my_turtle.pendown()

    Squre(3, 200)
    my_win.exitoneclick()

    return main


main()