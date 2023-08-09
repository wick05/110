# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program is a simple avatar maker!

def input_ui():
    """
    This is the main input/UI function. It asks the user all
    the questions pertaining to choosing their avatar, and calls the
    "print" functions for all the body parts based on the responses.
    :return: This function has no return value
    """

    print('----- AVATAR -----')

    # Using a while loop to validate initial user input. keep_asking is initially True, and
    # if the user input is valid, then keep_asking will become False in each condition.
    # If none of the conditions are valid, then there is no change to the default True value
    keep_asking = True
    while keep_asking:

        a_ask = input('Select an Avatar or create your own:\n')

        if a_ask == 'exit':
            keep_asking = False

        # the custom/create your own avatar case
        elif a_ask == 'custom':
            keep_asking = False
            print('Answer the following questions to create a custom avatar')

            # user inputs are stored in c_ "custom" variables

            # if the hat style isn't one of the valid responses, it defaults to front
            c_hat = str(input('Hat style ?\n'))
            if not ((c_hat == 'left') or (c_hat == 'right') or (c_hat == 'both') or (c_hat == 'front')):
                c_hat = 'front'

            c_eyes = input('Character for eyes ?\n')

            # for the hair, I chose to convert the string to a boolean
            c_hair = input('Long hair (True/False) ?\n')
            if c_hair == 'False':
                c_hair = False
            if c_hair == 'True':
                c_hair = True

            c_arms = input('Arm style ?\n')
            c_torso = int(input('Torso length ?\n'))
            c_leg = int(input('Leg length (1-4) ?\n'))
            c_shoe = str(input('Shoe look ?\n'))

            # once we've finished asking for all the custom user inputs, we use these values
            # as arguments when calling the body-part functions
            hat(c_hat)
            face(c_hair, c_eyes)
            arms(c_arms)
            torso(c_torso)
            legs(c_leg)
            shoe(c_shoe)

        # for the pre-built avatars, we can just hard-code the arguments for the
        # body-part functions, and display them based on the user's input string
        elif a_ask == 'Jeff':
            keep_asking = False
            hat('both')
            face(False, '0')
            # used the torso function for the neck
            torso(1)
            arms('=')
            torso(4)
            legs(2)
            shoe('#HHH#')

        elif a_ask == 'Jane':
            keep_asking = False
            hat('right')
            face(True, '*')
            arms('T')
            torso(2)
            legs(3)
            shoe('<|||>')

        elif a_ask == 'Chris':
            keep_asking = False
            hat('front')
            face(False, 'U')
            torso(1)
            arms('W')
            torso(2)
            legs(4)
            shoe('<>-<>')


def hat(hat_string):
    """
    This function takes in the 'left, 'right', 'both', or 'front' strings
    to output the hat.
    parameter hat_string - can be any string of the above options
    :return - has no return value
    """

    print('\n       ~-~       ')
    print('     /-~-~-\\     ')

    # conditional logic on if to print the left brim of the hat
    if hat_string == 'left' or hat_string == 'both':
        print(' ___', end='')
    else:
        print('    ', end='')

    print('/_______\\', end='')

    # conditional logic on if to print the right brim of the hat
    if hat_string == 'left' or hat_string == 'front':
        print('    ')
    else:
        print('___ ')


def face(hair_bool, eyes):
    """
    Takes a boolean hair variable to determine if long or short hair, and takes
    in a single character string to print the eye style
    :param hair_bool: any boolean
    :param eyes: any single character string
    :return: no return value
    """

    if hair_bool:
        print('   "|"""""""|"    ')
        print('   "| ' + eyes + '   ' + eyes + ' |"   ')
        print('   "|   V   |"    ')
        print('   "|  ~~~  |"    ')
        print('   " \\_____/ "   ')

    if not hair_bool:
        print("    |'''''''|    ")
        print('    | ' + eyes + '   ' + eyes + ' |    ')
        print('    |   V   |     ')
        print('    |  ~~~  |     ')
        print('     \\_____/     ')


def torso(torso_length):
    """
    This function prints the torso/neck portions vertically based on an integer torso_length
    :param torso_length: any positive integer
    :return: no return value
    """
    i = 1
    while i <= torso_length:
        print('      |-X-|      ')
        i += 1


def arms(arms_style):
    """
    This function prints arms based on a single character string arm style
    :param arms_style: should be any single character string
    :return: no return value
    """

    # printing the left side of the arms using a while loop
    print(' 0', end='')
    i = 1
    while i <= 4:
        print(arms_style, end='')
        i += 1

    print('|---|', end='')

    # printing the right side of the arms using a while loop
    i = 1
    while i <= 4:
        print(arms_style, end='')
        i += 1
    print('0')


def shoe(shoe_input):
    """
    This function prints shoes based on a 5 character shoe style
    :param shoe_input: any 5 character string
    :return: no return value
    """
    print(shoe_input + '       ' + shoe_input)


def legs(leg_length):
    """
    This function prints the legs based on the parameter leg_length
    :param leg_length: can be any integer 1-4
    :return: no return value
    """
    print('      HHHHH      ')

    i = 1
    while i <= leg_length:
        # since there are 5 characters to the left of the first part of the leg for a length of 1
        # we print 6-i spaces to start
        print((6-i)*' ', end='')
        print('///', end='')

        # since there's 1 space for a leg length of 1, and 3 for a length of 2, the spaces in
        # between legs are calculated with 1+2(i-1)
        print((1 + 2*(i-1)) * ' ', end='')
        print('\\\\\\')
        i += 1


def main():
    input_ui()


main()
