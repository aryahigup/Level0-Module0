import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    tammy = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    tammy.shape('circle')
    # Set your turtle's speed using .speed(2)
    tammy.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    tammy.color('green')
    tammy.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    tammy.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    tammy.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        tammy.forward(100)
        tammy.left(90)

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    tammy.goto(150,150)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    tammy.begin_fill()
    tammy.circle(30, steps=30)
    tammy.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    tammy.penup()
    tammy.goto(350,100)
    tammy.pendown()
    for i in range(5):
        tammy.forward(30)
        tammy.left(72)
    tammy.penup()
    tammy.goto(70,100)
    tammy.pendown()
    for i in range(6):
        tammy.forward(30)
        tammy.left(60)
    tammy.penup()
    tammy.goto(30,200)
    tammy.pendown()
    tammy.circle(45, steps=30)
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
