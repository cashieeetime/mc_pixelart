from turtle import *
# grid needa to be 128x128 blocks for map lvl 0

def set_origin(size):
    '''calculates start point for turtle'''
    x = size*128/-2
    y = size*128/2
    goto(x, y)

def draw_square(size):
    for i in range(4):
        forward(size)
        right(90)
    forward(size)

def draw_row(size):
    '''draws 1x128 row of squares'''
    for i in range(128):
        draw_square(size)

def next_row(size):
    '''positions turtle to draw the next row'''
    right(90)
    forward(size*2)

def draw_grid():
    '''main code to draw full 128x128 grid'''
    speed(0)
    size = 8
    penup()
    set_origin(size)
    pendown()

    draw_row(size)


done()