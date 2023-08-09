# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program contains the definition of multiple functions
#                   that draw various elements on the screen using the graphics.py module.
#                   It uses these functions to draw a day and night scene every time the birds
#                   fly by. The canvas is 750x500. Most elements take into account the user's
#                   cursor position to create a parallax effect.

from graphics import graphics
import random


def draw_bird_scrolling(object, origin):
    '''
    This function draws 5 birds flying left to right using 2 lines per bird. It takes the gui object
    and an x coordinate to begin the bird's flight.
    :param object: should be gui
    :param origin: an integer where the x origin is. In this case, this is 0 in def main()
    '''

    # using a while loop to offset each bird by 15 pixels down and right. Ends at 5 birds
    # the "y" offset is at a reduced rate (.5) to have a slight slope
    off = 0
    while off <= 75:
        object.line(origin - 10 + off, 200 + off/2, origin - 5 + off, 210 + off/2, 'black')
        object.line(origin - 5 + off, 210 + off/2, origin + off, 200 + off/2, 'black')
        off += 15


def draw_sun_parallax(object, color):
    '''
    This function draws the sun/moon using an ellipse, and takes into account the parallax effect.
    :param object: this should be the gui object
    :param color: this string can be any TKinter supported color
    :return:
    '''

    # using a 5-denominator parallax effect (LAYER 1), the most-buried layer
    x = (object.mouse_x/5) + 525
    y = (object.mouse_y/5)
    object.ellipse(x, y, 25, 25, color)


def draw_big_mountain(object, r, g, b):
    '''
    This function draws the big-center mountain using a triangle, taking into account the parallax effect.
    :param object: this should be the gui object
    :param r: red - this can be any integer 0-255
    :param g: green - this can be any integer 0-255
    :param b: blue - this can be any integer 0-255
    '''

    # converting the passed arguments into a color string
    mountain_color = object.get_color_string(r, g, b)

    # using a 4-denominator parallax effect (LAYER 2)
    x = object.mouse_x/4 + 306
    y = object.mouse_y/4 + 138
    object.triangle(x, y-50, x+400, y+300, x-400, y+300, mountain_color)


def draw_small_mountain_1(object, r, g, b):
    '''
    This function draws the right side mountain using a triangle, taking into account the parallax effect.
    :param object: this should be the gui object
    :param r: red - this can be any integer 0-255
    :param g: green - this can be any integer 0-255
    :param b: blue - this can be any integer 0-255
    '''

    # converting the passed arguments into a color string
    # intentionally mixing up the color arguments to create a unique color
    mountain_color = object.get_color_string(g, b, r)

    # using a level 3-denominator effect (LAYER 3)
    x = object.mouse_x/3 + 475
    y = object.mouse_y/3 + 107
    object.triangle(x, y, x+350, y+410, x-400, y+410, mountain_color)


def draw_small_mountain_2(object, r, g, b):
    '''
    This function draws the left side mountain using a triangle, taking into account the parallax effect.
    :param object: this should be the gui object
    :param r: red - this can be any integer 0-255
    :param g: green - this can be any integer 0-255
    :param b: blue - this can be any integer 0-255
    '''

    # converting the passed arguments into a color string
    # intentionally mixing up the color arguments to create a unique color
    mountain_color = object.get_color_string(b, r, g)

    # using a 3-denominator parallax effect (LAYER 3)
    x = object.mouse_x / 3 - 25
    y = object.mouse_y / 3 + 100
    object.triangle(x, y, x + 400, y + 415, x - 200, y + 415, mountain_color)


def draw_ground(object, color):
    '''
    This function draws the ground using a rectangle, taking into account the parallax effect.
    :param object: this should be the gui object
    :param color: this string can be any TKinter supported color
    '''

    # using a 2-denominator parallax effect (LAYER 4), the top parallax layer
    x = object.mouse_x / 2 - 385
    y = object.mouse_y / 2 + 275
    object.rectangle(x, y, 1200, 300, color)


def draw_grass(object, color):
    '''
    This function draws the grass along the top of the ground using lines and loops, taking
    into account the parallax effect. It uses slightly skewed lines(+3)
    :param object: should be the gui object
    :param color: this string can be any TKinter supported color
    '''

    # this is the x_coordinate starting point of the grass
    x_start = -200

    # using a 2-denominator parallax effect (LAYER 4), the top parallax layer
    x = object.mouse_x / 2 - 187
    y = object.mouse_y / 2 + 275

    # beginning off-screen -200 until we are well off-screen at 1000, we print a blade of grass
    # and then increment the x value by 10
    while x_start < 1000:
        object.line(x+x_start, y, x+x_start+3, y-15, color, 2)
        x_start += 10


def draw_tree(object, x_offset, y_offset, trunk_c, leaf_c):
    '''
    This function prints a tree. The x and y offset parameters are used for printing
    multiple trees in different positions. It uses a rectangle for the trunk, and an
    ellipse for the leaves.
    :param object: should be the gui object
    :param x_offset: this integer is how many x pixels to offset from the "base" tree
    :param y_offset: this integer is how many y pixels to offset from the "base" tree
    :param trunk_c: this string can be any TKinter supported color
    :param leaf_c: this string can be any TKinter supported color
    '''

    # using a 2-denominator parallax effect (LAYER 4), the top parallax layer
    x = object.mouse_x / 2 + 13
    y = object.mouse_y / 2 + 205
    object.rectangle(x + x_offset, y + y_offset, 20, 70, trunk_c)
    object.ellipse(x + 10 + x_offset, y + y_offset, 35, 65, leaf_c)


def draw_lit_firepit(object):
    '''
    This function draws a firepit with a flame, taking into account the parallax effect.
    It uses a line for the logs, and a triangle for the flame. Colors differ slightly
    from the unlit firepit.
    :param object: should be the gui object
    '''

    # using a 2-denominator parallax effect (LAYER 4), the top parallax layer
    # this has the same intended coordinates as the unlit firepit
    x = object.mouse_x / 2 + 263
    y = object.mouse_y / 2 + 325
    object.line(x, y, x+25, y-25, 'tan4', 5)
    object.line(x, y-25, x + 25, y, 'tan4', 5)
    object.triangle(x+12, y-35, x+20, y-12, x+5, y-12, 'yellow')


def draw_unlit_firepit(object):
    '''
    This function draws a firepit without a flame, taking into account the parallax effect.
    It uses a line for the logs. Colors differ slightly from the lit firepit.
    :param object: should be the gui object
    '''

    # using a 2-denominator parallax effect (LAYER 4), the top parallax layer
    # this has the same intended coordinates as the lit firepit
    x = object.mouse_x / 2 + 263
    y = object.mouse_y / 2 + 325
    object.line(x, y, x+25, y-25, 'tan3', 5)
    object.line(x, y-25, x + 25, y, 'tan3', 5)


def draw_sky(object, color):
    '''
    This function draws the background/sky using a rectangle.
    :param object: this should be the gui object
    :param color: this string can be any TKinter supported color
    '''
    object.rectangle(0, 0, 750, 500, color)


def main():

    # initializing all of my starter variables
    gui = graphics(750, 500, "Day 'N' Nite")
    # having the birds start at x=0
    bird_x_coord = -100

    # generating one set of random color values. These are mixed/swapped
    # in the arguments for the mountains, so that these values produce
    # effectively 3 different colors. I take random values between 100 and 255
    # because nighttime switches the colors down by -100, so I don't want to be
    # out of scope.
    random_r = random.randint(100, 255)
    random_g = random.randint(100, 255)
    random_b = random.randint(100, 255)

    # the program starts as daytime, and turns to night once the birds
    # finish their flight across the screen
    day = True

    # this is the master infinite while loop that prints objects 30 frames per second
    while True:
        gui.clear()

        if day:

            # drawing all of the elements on the screen in proper order, with colors
            # that correspond to daytime, and with an unlit firepit
            draw_sky(gui, 'paleturquoise1')
            draw_sun_parallax(gui, 'light goldenrod')
            draw_big_mountain(gui, random_r, random_g, random_b)
            draw_small_mountain_1(gui, random_r, random_g, random_b)
            draw_small_mountain_2(gui, random_r, random_g, random_b)
            draw_ground(gui, 'lawn green')
            draw_grass(gui, 'yellow green')
            draw_tree(gui, 0, 10, 'sienna2', 'darkorange1')
            draw_tree(gui, -150, 50, 'sienna3', 'chartreuse2')
            draw_tree(gui, 100, 25, 'sienna3', 'darkorange1')
            draw_tree(gui, 400, 30, 'sienna2', 'orangered2')
            draw_unlit_firepit(gui)

            # drawing the birds, and then iterating their x coordinates by 5
            draw_bird_scrolling(gui, bird_x_coord)
            bird_x_coord += 5

            # once the x coordinate is above 850, then we invert the day value
            # and reset the x coordinate to -100
            if bird_x_coord > 850:
                day = False
                bird_x_coord = -100

        else:

            # drawing all of the elements on the screen in proper order, with colors
            # that correspond to nighttime, and with a lit firepit
            draw_sky(gui, 'midnight blue')
            draw_sun_parallax(gui, 'snow')
            draw_big_mountain(gui, random_r-100, random_g-100, random_b-100)
            draw_small_mountain_1(gui, random_r-100, random_g-100, random_b-100)
            draw_small_mountain_2(gui, random_r-100, random_g-100, random_b-100)
            draw_ground(gui, 'dark green')
            draw_grass(gui, 'dark olive green')
            draw_tree(gui, 0, 10, 'sienna4', 'darkorange3')
            draw_tree(gui, -150, 50, 'sienna4', 'chartreuse4')
            draw_tree(gui, 100, 25, 'sienna4', 'darkorange3')
            draw_tree(gui, 400, 30, 'sienna4', 'orangered4')
            draw_lit_firepit(gui)

            # drawing the birds, and then iterating their x coordinates by 5
            draw_bird_scrolling(gui, bird_x_coord)
            bird_x_coord += 5

            # once the x coordinate is above 850, then we invert the day value
            # and reset the x coordinate to -100
            if bird_x_coord > 850:
                day = True
                bird_x_coord = -100

        # 30 frames per second
        gui.update_frame(30)


main()
