#This is a program that draws a delicious pizza using turtle art.
#Author: YunShan Nong

import turtle

#functions
def wheel(t, side_length):
    """(Turtle, int) -> NoneType
    A function that takes a turtle object and a designed side length,
    and draws a polygone with repetitive parts.
    """
    for i in range(10):
        for i in range(2):
            t.forward(side_length)
            t.right(120)
            t.forward(side_length)
            t.right(60)
        t.right(30)
        
    # x = x position, y = y position
def leaves(t, radius, color, degrees, x, y):
    """(Turtle, float, str, float, float, float) -> NoneType
    A function that takes a turtle object, 4 floats and a string
    representing a colors as inputs, and draws a shape similar
    to leaves with design radius and degrees.
    """
    t.hideturtle()
    t.penup()
    t.speed(8.5)
    t.goto(x, y)
    t.pendown()
    t.pensize(2)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.circle(radius, degrees)
        t.left( 180 - degrees)
        t.circle(radius, degrees)
    t.right(180 - degrees)
    t.end_fill()

def oval(t, x, y, big_radius, small_radius, color, angle):
    """(Turtle, float, flaot, float, float, str, float) -> NoneType
    a function that takes a turtle object, 5 floats and a string
    representing a color as inputs, and draws an oval.
    """
    t.hideturtle()
    t.speed(7.0)
    t.pensize(3)
    t.penup()
    t.fillcolor(color)
    t.goto(x,y)
    t.left(angle)
    t.pendown()
    t.begin_fill()
    t.circle(big_radius,90)
    t.circle(small_radius,90)
    t.circle(big_radius,90)
    t.circle(small_radius,90)
    t.end_fill()
    
def pepperoni(t, x, y, radius, color):
    """"(Turtle, float, float, float, string) -> NoneType
    a functions taking a turtle object, 3 floats and a string representing
    a color as inputs, and draws a circle.
    """
    t.hideturtle()
    t.speed(7.0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pensize(3)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
def arc(t, x, y, angle, color, radius):
    """(Turtle, float, float, float, string, float) -> NoneType
    a functions taking a turtle object, 4 floats and a string representing
    a color as inputs, and draws a half-circle.
    """
    t.speed(7.0)
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(color)
    t.pensize(3)
    t.begin_fill()
    t.left(angle)
    t.circle(radius,180)
    t.left(90)
    t.forward(radius*2)
    t.end_fill()
    
#my_artwork
def my_artwork():
    """"() -> NoneType
    a functions taking nothing as inputs, and draws a pizza inside
    a pizza_box
    """
    #pizza box (in the background)
    pizza_box = turtle.Turtle()
    pizza_box.hideturtle()
    pizza_box.shape("circle")
    pizza_box.pensize(6)
    pizza_box.fillcolor("bisque3")
    pizza_box.begin_fill()
    pizza_box.speed(10.35)
    wheel(pizza_box, 350)
    pizza_box.end_fill()

    #pizza_side
    pizza_side = turtle.Turtle()
    pizza_side.hideturtle()
    pizza_side.penup()
    pizza_side.goto(0, -270)
    pizza_side.pendown()
    pizza_side.pensize(4)
    pizza_side.fillcolor("tan1")
    pizza_side.begin_fill()
    pizza_side.speed(9.5)
    pizza_side.circle(270)
    pizza_side.end_fill()

    #pizza
    pizza = turtle.Turtle()
    pizza.hideturtle()
    pizza.penup()
    pizza.speed(9.5)
    pizza.goto(0, -240)
    pizza.pendown()
    pizza.pensize(2)
    pizza.fillcolor("moccasin")
    pizza.begin_fill()
    pizza.pensize(4)
    pizza.circle(240)
    pizza.end_fill()
    pizza.pendown()

    #pepperoni (5)
    pepperoni1 = turtle.Turtle()
    pepperoni(pepperoni1, 125, 55, 44, "firebrick")
    pepperoni2 = turtle.Turtle()
    pepperoni(pepperoni2, -100, 80, 48, "maroon")
    pepperoni3 = turtle.Turtle()
    pepperoni(pepperoni3, -110, -150, 42, "firebrick")
    pepperoni4 = turtle.Turtle()
    pepperoni(pepperoni4, 120, -155, 48, "maroon")
    pepperoni5 = turtle.Turtle()
    pepperoni(pepperoni5, 5, -30, 44, "firebrick")

    #pineapples (4)
    pineapple1 = turtle.Turtle()
    arc(pineapple1, 70, 150, 80, "yellow", 55)
    pineapple2 = turtle.Turtle()
    arc(pineapple2, -75, 40, 140, "yellow", 50)
    pineapple3 = turtle.Turtle()
    arc(pineapple3, 150, -30, -20, "yellow1", 55)
    pineapple4 = turtle.Turtle()
    arc(pineapple4, -65, -160, -110, "yellow", 50)

    #olives (5)
    olive1 = turtle.Turtle()
    olive2 = turtle.Turtle()
    olive3 = turtle.Turtle()
    olive4 = turtle.Turtle()
    olive5 = turtle.Turtle()
    oval(olive1, 5, 85, 25, 10, "DarkOliveGreen", 0)
    oval(olive2, 50, -185, 20, 8, "DarkOliveGreen", -30)
    oval(olive3, 100, -15, 20, 9, "DarkOliveGreen", 10)
    oval(olive4, -80, -30, 19, 8, "DarkOliveGreen", -70)
    oval(olive5, -195, -70, 16, 7, "DarkOliveGreen", -50)

    #leaves (2)
    leaf1 = turtle.Turtle()
    leaves(leaf1, 35, "sea green", 70, -180, 70)
    leaf2 = turtle.Turtle()
    leaves(leaf2, 60, "seagreen3", -60, 10, -100)

    #Y-letter (signature)
    y_letter= turtle.Turtle()
    y_letter.penup()
    y_letter.goto(330,-250)
    y_letter.pendown()
    y_letter.color("orangered")
    y_letter.pensize(6)
    y_letter.left(45)
    y_letter.forward(30)
    y_letter.backward(30)
    y_letter.left(90)
    y_letter.forward(30)
    y_letter.backward(30)
    y_letter.left(135)
    y_letter.forward(45)
    y_letter.left(-180)
    y_letter.circle(20,-120)

#start drawing
my_artwork()