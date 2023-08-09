# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program receives a "hit string" which are coordinates that are
#                   shot at a target. It validates the "hit string" so its of proper format,
#                   and then prints out the target with the "hits" on it. The hit markers
#                   are any 1-digit character selected by the user.

# creating a "keep_asking" variable that gets turned off when they provide a valid hit string
keep_asking = 1

# this "hit string" loop will keep running as long as keep_asking is 1
while keep_asking == 1:

    # prompting the user for a hit string
    full_hit_string = input('Hit string:\n')

    # if the hit string is smaller than 4 units, or not a multiple of 4 (using modulus 4 != 0)
    # then it gives the error message and keeps asking
    if len(full_hit_string) < 4 or (len(full_hit_string)) % 4 != 0:
        print('Please provide a valid hit string.')

    # otherwise, if the hit string is a valid input, keep_asking is 0, and we exit the loop
    else:
        keep_asking = 0


# setting keep_asking back to 1, recycling the variable in the loop for the marker prompt
keep_asking = 1

# this "marker" loop will keep running as long as keep_asking is 1
while keep_asking == 1:

    # prompting the user for the marker
    marker = input('Marker:\n')

    # if the length of the marker is not 1, prints the error message and keeps asking
    if len(marker) != 1:
        print('Please provide a valid marker.')

    # otherwise, if the marker length is 1, sets keep_asking to 0
    else:
        keep_asking = 0

# hits_so_far is 0. this variable will be used to move the hit string forward by 4 characters
# every time a hit happens
hits_so_far = 0

# using a 4 character long section, spliced out of the user's full hit string
# the hit string section will be advanced by 4 characters with every hit
hit_string_section = full_hit_string[0:4]

# x value is first 2/4 of the 4-character hit string section
current_hit_x = int(hit_string_section[0] + hit_string_section[1])
# y value is second 2/4 of the 4-character hit string section
current_hit_y = int(hit_string_section[2] + hit_string_section[3])

# starter index_row is the highest "y" value of 5, top to bottom
index_row = 5

# starter index_column is the lowest "x" value of -7, left to right
index_column = -7

# outer "row" loops as long as the index_row is in the range of [-5,5] (starts at +5)
while index_row >= -5:
    # inner "column" loops as long as the index_columns are in the range of [-7,7] (starts at -7)
    while index_column <= 7:

        # setting the print_me variable to a blank space by default
        print_me = ' '

        # if the row index is in the middle "0" row, the default print_me variable is a dash
        if index_row == 0:
            print_me = '-'

        # if the column index is in the middle "0" column, the default print_me variable is a vertical line
        if index_column == 0:
            print_me = '|'

        # if the index row and column matches the current hit
        if index_row == current_hit_y and index_column == current_hit_x:

            # setting the print_me variable to match the marker that the user inputted earlier
            print_me = marker

            # incrementing hits_so_far by 1, so we can move along to the next 4-character segment next time
            hits_so_far += 1

            # setting the new hit section/splice to be 4 spaces ahead of the previous in the full string
            hit_string_section = full_hit_string[(0+(hits_so_far*4)):(4+(hits_so_far*4))]

            # if the length of the new hit string section is not blank, then we set the new
            # current hits x and y to the new valid string section. if we don't do this if
            # then we will set the current hits to an out-of-scope section of the full_hit_string
            if len(hit_string_section) != 0:

                # setting the current x and y hit coordinates to the new hit section
                current_hit_x = int(hit_string_section[0] + hit_string_section[1])
                current_hit_y = int(hit_string_section[2] + hit_string_section[3])

        # if we're on the last index column, aka the end of the line, then we want to print
        # with a newline
        if index_column == 7:
            print(print_me)

        # otherwise, if we're not on the last index column, we don't want to print a newline
        else:
            print(print_me, end='')

        # incrementing the column by +1, so we can move on to the next space in the line
        index_column += 1

    # need to reinitialize the index column back to -7 after it finishes its inner loop
    # otherwise it's still at the max index_column value
    index_column = -7

    # finally, iterating the index_row by -1 to move on to the next line of the output
    index_row -= 1
