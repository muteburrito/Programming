import turtle

bob = turtle.Turtle()

bob.color("red", "orange")

bob.begin_fill()

bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)

bob.penup()
bob.forward(100)
bob.pendown()

bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)

bob.end_fill()

turtle.done()