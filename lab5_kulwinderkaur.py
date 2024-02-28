"""
Lab 5 - Code Refactoring
(100 marks in total)

Name:
Due Data: Feb. 9, 2023, 11:00am

Objective:

Code refactoring in software development is to restructure code to 
a simpler, cleaner or more expressive architecture while keeping
its original functionality.

In this lab, the original code creates a beautiful symmetric drawing
(sometimes called mandala). You will notice that there is a lot of 
code repetition.

Your task is to rewrite the code so it still draws the same picture, 
but it uses only two functions. Each of the functions you write 
has to be very short (about 4 lines of code). In order to 
accomplish that, you need to add additional parameters to each function.

To start, figure out what the current function parameters do. 
Then figure out how the functions are different and how you can 
introduce new parameters to have only one function that 
replaces all the ones with the same name.

In the final program you submit, you should be able to change 
only one line of code in order to produce a drawing that contains
a different number of petals.

"""

import turtle

"""
Exercise 1:

Notice that all draw_circles functions are practically the same,
except for the number of circles drawn and the resizing in each 
for loop iteration. 

Write a function called draw_circles to replaces all of the functions. 
draw_circles should have one additional parameters to accommodate
these varying values, and it should have about 4 lines of code.
"""

# t=turtle.Turtle()
def draw_circles(t, size,decrease_amount):
    for _ in range(4):
        t.circle(size)
        size= size - decrease_amount

# draw_circles(t,200,10)
# def draw_circles5(t, size):
#     for _ in range(4):
#         t.circle(size)
#         size = size - 5


# def draw_circles10(t, size):
#     for _ in range(4):
#         t.circle(size)
#         size = size - 10


# def draw_circles19(t, size):
#     for _ in range(4):
#         t.circle(size)
#         size = size - 19


# def draw_circles20(t, size):
#     for _ in range(4):
#         t.circle(size)
#         size = size - 20




"""
Exercise 2:

Similar to Exercise 1, replace all instances of draw_special function with one 
function that uses parameters. Your function must call the drawCircle function 
you developed in exercise 1.

The function draw_special you write is short as well (about 4 lines of code).

"""


def draw_special(t, size, repeat,decrease_amount):
    for _ in range(repeat):
        draw_circles(t, size,decrease_amount)
        t.right(360 / repeat)

# draw_special(t,200,4,10)

# def draw_special5(t, size, repeat):
#     for _ in range(repeat):
#         draw_circles5(t, size)
#         t.right(360 / repeat)


# def draw_special10(t, size, repeat):
#     for _ in range(repeat):
#         draw_circles10(t, size)
#         t.right(360 / repeat)


# def draw_special19(t, size, repeat):
#     for _ in range(repeat):
#         draw_circles19(t, size)
#         t.right(360 / repeat)


# def draw_special20(t, size, repeat):
#     for _ in range(repeat):
#         draw_circles20(t, size)
#         t.right(360 / repeat)

# def draw_special(t, size, repeat, decrease_amount):
#     pass

"""
Exercise 3:

At this point, you would have created 2 new functions: draw_circles and draw_special.

Your job is now to rewrite draw_picture() below so that it uses the 2 new functions 
from Exercises 1 and 2.

The rewritten version of draw_picture() will also meet the following constraints:

  - Use 1 turtle instead of multiple turtles

  - Use a loop to change the turtle color and the decreasing amounts. 


HINT: 

You may either write a compound if statement inside the 
body of the loop to control how each color is drawn such as: 

        ...
        colours = ['white', 'yellow', 'blue', 'orange', 'pink']
        for c in colours:
            t.color(c)
            ...
            
or use 2 lists to avoid the if statement, which is recommended:
        ...
        colours = ['white', 'yellow', 'blue', 'orange', 'pink']
        decrease_amounts = [4, 10, 5, 19, 20]
        for i in range(5):
            t.color(colours[i])
        ...

"""


def draw_picture():

    wn = turtle.Screen()
    wn.bgcolor('black')
    t= turtle.Turtle()
    t.speed(20)
    size=100
    repeat=10
    decrease_amounts = [4, 10, 5, 19, 20]
    colors=['white', 'yellow', 'blue', 'orange', 'pink']
    for i in range(5):
        t.color(colors[i])
        draw_special(t,size,repeat,decrease_amounts[i])

    # Steve = turtle.Turtle()
    # Steve.speed(10)
    # Steve.color('yellow')
    # draw_special10(Steve, 100, 10)

    # Barry = turtle.Turtle()
    # Barry.speed(0)
    # Barry.color('blue')
    # draw_special5(Barry, 100, 10)

    # Terry = turtle.Turtle()
    # Terry.speed(0)
    # Terry.color('orange')
    # draw_special19(Terry, 100, 10)

    # Will = turtle.Turtle()
    # Will.speed(0)
    # Will.color('pink')
    # draw_special20(Will, 100, 10)

    wn.exitonclick()


draw_picture()

"""
Hope this lab will be helpful to your project 1 - Artistic Turtle Drawing.
Have fun!

If you have any course feedback for the instructor, feel free to input here:
https://comp115-bravo.github.io/

Please note that you don't need to submit your github link of your every lab,
as long as you get marks for your labs, Alice knows your GitHub link. Just to
save you a tiny bit of time.




"""