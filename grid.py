from turtle import *

##############################################
# SET DEFAULTS
##############################################

def set_origin(size, size2):
    '''calculates start point for turtle'''
    x = size*size2/-2
    y = size*size2/2
    goto(x, y)

##############################################
# DRAWING & MUTATING SQUARES
##############################################

def draw_square(size):
    '''draws one square of given size'''
    for i in range(4):
        forward(size)
        right(90)
    forward(size)

def goto_square(size):
    '''tells turtle which square to go to based on x&y'''
    x = int(input("Enter an x value: "))
    y = int(input("Enter an y value: "))
    
    forward((x*size)-size)
    right(90)
    forward((y*size)-size)
    left(90)

def fill_square(size):
    '''fills square with color of user's choice'''
    color = input("Enter a color or hex code: ")
    old_fill = fillcolor()
    old_pen = pencolor()
    begin_fill()
    draw_square(size)
    end_fill()
    color(old_pen, old_fill)

##############################################
# DRAWING & MUTATING ROWS
##############################################

def draw_row(size, size2):
    '''draws 1 row of squares'''
    for i in range(size2):
        draw_square(size)

def next_row(size, size2):
    '''positions turtle to draw the next row'''
    right(90)
    forward(size)
    right(90)
    forward(size*size2)
    right(180)

##############################################
# DRAWING GRID
##############################################

def draw_grid(size, size2):
    '''main code to draw full 128x128 grid'''
    speed(0)
    #hideturtle()
    penup()
    set_origin(size, size2)
    pendown()
    for i in range(size2):
        draw_row(size, size2)
        next_row(size, size2)
    set_origin(size, size2)

##############################################
# MAIN
##############################################

def main():
    size = 100  # size for one side of each grid square
    size2 = 5   # number of square per row

    draw_grid(size, size2)

    while True:
        goto_square(size)
        fill_square(size)
        set_origin(size, size2)
        answer = input("Continue?\n-> ")
        if answer.lower() == "y" or answer.lower() ==  "":
            continue
        else:
            break

main()
done()