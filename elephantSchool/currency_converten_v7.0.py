"""
    分形树
"""

import turtle

def branch(length,branch_size):
    if length > 5:
        if branch_size < 2:
            turtle.pencolor('green')
        else:
            turtle.pencolor('brown')
        turtle.pensize(branch_size)
        turtle.forward(length)
        turtle.right(20)
        branch_size-=1
        branch(length - 15,branch_size)

        turtle.left(40)
        branch(length - 15,branch_size)

        turtle.right(20)
        if branch_size < 1:
            turtle.pencolor('green')
        else:
            turtle.pencolor('brown')
        turtle.backward(length)


def main():

    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pencolor('brown')
    branch(100,7)
    turtle.exitonclick()

if __name__ == '__main__':
    main()