"""
Lab 3: Draw some basic shapes with Turtle Graphics, using loop algorithms.

Complete exercise 1-4 (each values 25 points, 100 points in total).

The exercise 5 is an optional challenge.

Note: 1. Please do not change the function definition.
      2. You can see the lab3 result demo here: https://comp115-bravo.github.io/lab3_demo.html
      3. Upload your lab3 to your GitHub's repository when you finish, similar to lab1 and lab2.

Author:  <your name>
Due Date: This Friday (Jan. 26) 11am.
    
"""

import turtle

window = turtle.Screen()

"""
Understanding the following two examples is beneficial for you to 
move onto the exercises below.

This is an example that uses turtle to draw steps of 10 pixels by 10 pixels. 
"""


def draw_steps(num_steps):
    pen = turtle.Turtle()
    pen.speed(1)  # 1 sets the drawing speed as the slowest.
    for _ in range(num_steps):
        pen.forward(10) # 10 pixels
        pen.left(90) # Angle
        pen.forward(10)
        pen.right(90)
    pen.shape("blank")  # After drawing, make the pen invisible.
    pen.clear()  # Clear the drawing on the screen.


draw_steps(3)  # Call function draw_steps() with an argument 3 passing to num_steps


"""
This is another example drawing an equilateral triangle,
which we have discussed during the lecture: 
"""

def draw_triangle(side_length):
    """ This function draws an equilateral triangle, 
    of which the side length equals the argument side_length.
    """
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / 3  # Calculate the exterior angle of an equilateral triangle.
    for _ in range(3):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()

draw_triangle(20)


"""
Exercise 1 (25 points)

Similar to the previous examples, but to draw a square instead. 
To draw a square is very similar to draw an equilateral triangle. 
We need to calculate the exterior angle of a square,
which is 90 degrees, the angle your turtle pen will turn.

Your task is to replace pass with a for-loop, making 
function draw_square(side_length) able to draw a square given any side_length.

If you need, you can review the concept of exterior angles of regular polygons from here:
https://www.teachoo.com/8592/2789/Exterior-Angles-of-Regular-Polygons/category/Sum-of-Exterior-Angles-of-Polygons/
"""

def draw_square(side_length):
    """ Draw a square whose side length equals the value of side_length """
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / 4 # Calculate the exterior angle of a square
    for _ in range(4):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()


draw_square(20)



"""
Exercise 2 (25 points)

Similar as exercise 1, 
but draw an arbitrary regular polygon when given a number of sides and a side length.

Your task is to replace pass with a for-loop, making 
function draw_regular_polygon(num_sides, side_length) able to draw an arbitrary regular polygon.

"""
def draw_regular_polygon(num_sides, side_length):
    """ Draw an arbitrary regular polygon,
    when given a number of sides, and a side_length"""
    pen = turtle.Turtle()
    pen.speed(1)
    exterior_angle = 360 / num_sides  # Calculate the exterior angle of a regular polygon
    for _ in range(num_sides):
        pen.forward(side_length)
        pen.left(exterior_angle)
    pen.shape("blank")
    pen.clear()


draw_regular_polygon(6, 20)

"""
Exercise 3 (25 points)

This time, draw a rectangle of the specified length and width
Try to identfy where you can use a for-loop.

"""
def draw_rectangle(length, width):
    pen = turtle.Turtle()
    pen.speed(1)
    for _ in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)
    pen.shape("blank")
    pen.clear()


draw_rectangle(20, 10)


"""
Exercise 4 (25 points)

Replace pass with function body to make the function draw_circles(num_circles)
draw a number of circles. All the circles starts from the origin (the same point) 
to draw. The first circle's radius is 10 pixels, and the radiuses of the following 
circles are increasing by 5 pixels.

For example, draw_circles(3) will draw 3 circles. The radius of the first one is 10,
and the radius of the second one is 10 + 5 = 15, and the radius of the third one
is 15 + 5 = 20. 

Another example, draw_circles(5) will draw 5 circles.
The radius of the first one is 10, and the radius of the second one is 10 + 5 = 15,
and the radius of the third one is 15 + 5 = 20, and the fourth radius is 20 + 5 = 25,
and the fifth radius is 25 + 5 = 30.

Hint: 
1. We can use pen.circle(radius) to draw a circle whose radius equals the argument 'radius'.
2. Think about how we should increase the radius in the for-loops.

"""
def draw_circles(num_circles):
    radius = 10 # The first circle's radius is 10 pixels.
    radius_increase = 5
    pen = turtle.Turtle()
    pen.speed(1)
    for _ in range(num_circles):
        pen.circle(radius)
        radius = radius + radius_increase
    pen.shape("blank")
    pen.clear()


draw_circles(5)


"""
Exercise 5 (Optional challenge)

This time, draw a number of concentric circles, by completing the for-loop below.

Hint: pen.up() lifts the pen up; 
      pen.down() puts the pen down, ready for drawing.

"""
def draw_concentric_circles(num_circles):
    radius = 10
    radius_increase = 5
    pen = turtle.Turtle()
    pen.speed(5)
    pen.up()
    for _ in range(num_circles):
        pen.goto(0, -radius)
        pen.down()
        pen.circle(radius)
        radius = radius + radius_increase
        pen.up()

    pen.shape("blank")
    pen.clear()

draw_concentric_circles(6)

window.exitonclick()