"""
    绘制五角星
"""
import turtle

def draw(size):
    count = 0
    while count < 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main(width):

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    while width < 100:
        draw(width)
        width += 10
    turtle.exitonclick()


if __name__ == '__main__':
    main(50)