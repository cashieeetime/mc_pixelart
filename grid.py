from turtle import *
# grid needa to be 128x128 blocks for map lvl 0

def set_origin(size, size2):
    '''calculates start point for turtle'''
    x = size*size2/-2
    y = size*size2/2
    goto(x, y)

def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
    forward(size)

def draw_row(size, size2):
    '''draws 1x128 row of squares'''
    for i in range(size2):
        draw_square(size)

def next_row(size, size2):
    '''positions turtle to draw the next row'''
    right(90)
    forward(size)
    right(90)
    forward(size*size2)
    right(180)

def goto_square(size):
    pass

def draw_grid():
    '''main code to draw full 128x128 grid'''
    size = 10      # size for one side of each individual grid square
    size2 = 10   # number of square per row
    speed(0)
    hideturtle()
    penup()
    set_origin(size, size2)
    pendown()
    for i in range(size2):
        draw_row(size, size2)
        next_row(size, size2)

draw_grid()
done()