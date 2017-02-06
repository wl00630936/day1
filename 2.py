import turtle

def draw_square(t, size):
        for i in range(4):
                t.forward(size)
                t.left(90)

window = turtle.Screen()
window.bgcolor("lightblue")

john = turtle.Turtle()
draw_square(john, 50)

john.penup()
john.forward(100)

john.pendown()
draw_square(john, 50)

john.penup()
john.forward(100)

john.pendown()
draw_square(john, 50)

window.exitonclick()
 
