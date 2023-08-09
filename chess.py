# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program is a 1-d chess game that takes the users input for the
#                   position of the piece to be moved, and the direction to move it. It
#                   shows 2 UIs, one in the console, and one using the graphics library.

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'


def is_valid_move(board, position, player):
    '''
    This function determines if the users input is a valid move
    :param board: should be a list of strings with list length of 9
    :param position: should be an integer between 0 and 8 inclusive
    :param player: should be WHITE or BLACK
    :return: returns True or False based on if valid move
    '''

    # if the players input is out of range, invalid
    if (position > 8) or (position < 0):
        return False

    # if the value in the list at the players position doesn't correspond to
    # their color, then the move is invalid
    if player == WHITE:
        if board[position] != W_KNIGHT and board[position] != W_KING:
            return False
        else:
            return True

    # same as above for black
    elif player == BLACK:
        if board[position] != B_KNIGHT and board[position] != B_KING:
            return False
        else:
            return True


def move_knight(board, position, direction):
    '''
    This function moves the knight based on the user's input position and direction
    :param board: should be a list of strings with list length of 9
    :param position: should be an integer between 0 and 8 inclusive
    :param direction: should be RIGHT or LEFT
    :return: no return value
    '''

    # if the knight is trying to move right and the move would NOT put the piece
    # out of scope, then we move the piece by 2 places and erase the old space
    if direction == RIGHT:
        if not (position + 2) > 8:
            board[position+2] = board[position]
            board[position] = EMPTY

    # same as above for going left, with altered logic for the lower scope
    if direction == LEFT:
        if not (position - 2) < 0:
            board[position-2] = board[position]
            board[position] = EMPTY


def move_king(board, position, direction):
    '''
    This function moves the king based on the users input position and direction.
    :param board: should be a list of strings with list length of 9
    :param position: should be an integer between 0 and 8 inclusive
    :param direction: should be RIGHT or LEFT
    :return: no return value
    '''

    # for moving right, the king only will move if they're not on the last index
    if (direction == RIGHT) and (position != 8):

        # this case is when there is a piece adjacent to the king on the right
        if board[position+1] != EMPTY:
            board[position+1] = board[position]
            board[position] = EMPTY

        # otherwise, there are 2 cases for when there is a space on the right of the king
        else:

            # this case tests if there are spaces until the end of the list
            # it is necessary for no out-of-scope checking
            # testing the spaces to the right of the king
            test_position = position+1
            full_slide = True

            while test_position < 9:
                # if we detect a non-EMPTY, then its not a "full-slide"
                if board[test_position] != EMPTY:
                    full_slide = False
                test_position += 1

            # if full_slide is still true, we move the king to the last list index
            if full_slide:
                board[8] = board[position]
                board[position] = EMPTY

            # otherwise, if it's not a full_slide situation, then we
            # are doing the regular check, where we look for a space to the right, and
            # if there's a piece after it, then we occupy that pieces space
            else:
                test_position = position
                while test_position < 9:

                    # checking that the current test position is empty, and the following
                    # space is not empty. if both are true, we occupy that following space.
                    # we also set test_position to 9 to break the loop, so we ensure
                    # that the king moves to the first situation detected like this
                    if board[test_position] == EMPTY and board[test_position+1] != EMPTY:
                        board[test_position+1] = board[position]
                        board[position] = EMPTY
                        test_position = 9
                    
                    test_position += 1

    # the rest of this function is mirrored logic to the RIGHT portion above
    # initial check if they're trying to move left while on space 0
    if (direction == LEFT) and (position != 0):

        # adjacent piece check
        if board[position-1] != EMPTY:
            board[position-1] = board[position]
            board[position] = EMPTY

        else:

            # full-slide check, where there's only spaces to the left of the king
            test_position = position-1
            full_slide = True

            while test_position > 0:
                if board[test_position] != EMPTY:
                    full_slide = False
                test_position -= 1
                
            if full_slide:
                board[0] = board[position]
                board[position] = EMPTY

            # regular check where we are looking for spaces to the left and pieces after
            else:
                test_position = position
                while test_position > 0:

                    if board[test_position] == EMPTY and board[test_position-1] != EMPTY:
                        board[test_position-1] = board[position]
                        board[position] = EMPTY
                        test_position = 0

                    test_position -= 1


def print_board(board):
    '''
    This function prints the console screen based on the elements in the list
    :param board: should be a list of strings with list length of 9
    '''

    # using a 3 iteration long while loop to print out the rows
    row = 1
    while row <= 3:

        # for the first and third rows
        if row == 1 or row == 3:
            i = 0
            # the console string length is 54 characters. checking which character
            # we are on and displaying the according symbol
            while i < 55:
                if i == 0:
                    print('+', end='')
                elif i == 54:
                    # printing the end line if we're on the last space
                    print('+')
                else:
                    print('-', end='') 
                i += 1

        # row 2 for displaying the list
        if row == 2:
            i = 0

            # chopped it into 9 spaces, printing the corresponding element
            # in the list
            while i < 9:
                if i == 8:
                    # printing the end line and final '|' if on the last element
                    print('| ' + board[i] + ' |')
                else:
                    print('| ' + board[i] + ' ', end='')
                i += 1

        row += 1


def draw_board(board, gui):
    '''
    This function draws the gui version of the board, based on the graphics object
    and the board passed in to this function.
    :param board: should be a list of strings with list length of 9
    :param gui: should be gui
    :return: no return value
    '''

    # drawing the white background, and the text
    gui.rectangle(0, 0, 700, 200, 'white')
    gui.text(280, 50, '1-D Chess', 'brown', 20)

    # drawing the squares, and the left-border edge of the squares using a while loop
    i = 0
    while i < 9:
        gui.rectangle((125+50*i), 100, 50, 50, 'brown')
        gui.line((125 + 50 * i), 100, (125 + 50 * i), 150, 'black', 2)
        i += 1

    # drawing the whole top edge, whole bottom edge, and far right borders of the squares
    gui.line(575, 100, 575, 150, 'black', 2)
    gui.line(125, 100, 575, 100, 'black', 2)
    gui.line(125, 150, 575, 150, 'black', 2)

    # using a while loop and if statement to draw the icons of the pieces
    # corresponding to their respective values in the list at each location
    i = 0
    while i < 9:
        if board[i] == W_KING:

            # drawing a "crown" looking piece instead of text for the white king
            gui.line((125+20+50*i), 135, (125+10+50*i), 115, 'white', 3)
            gui.ellipse((125+10+50*i), 115, 6, 6, 'white')
            gui.line((125 + 25 + 50 * i), 135, (125 + 25 + 50 * i), 110, 'white', 3)
            gui.ellipse((125 + 25 + 50 * i), 110, 6, 6, 'white')
            gui.line((125 + 30 + 50 * i), 135, (125 + 40 + 50 * i), 115, 'white', 3)
            gui.ellipse((125 + 40 + 50 * i), 115, 6, 6, 'white')
            gui.ellipse((125 + 25 + 50 * i), 135, 20, 4, 'white')

        if board[i] == W_KNIGHT:

            # drawing a "pawn" looking piece for the white knight
            gui.line((125 + 25 + 50 * i), 135, (125 + 25 + 50 * i), 110, 'white', 3)
            gui.ellipse((125 + 25 + 50 * i), 110, 6, 6, 'white')
            gui.ellipse((125 + 25 + 50 * i), 135, 20, 4, 'white')

        if board[i] == B_KING:

            # drawing the same crown as white, but in black, for the black king
            gui.line((125+20+50*i), 135, (125+10+50*i), 115, 'black', 3)
            gui.ellipse((125+10+50*i), 115, 6, 6, 'black')
            gui.line((125 + 25 + 50 * i), 135, (125 + 25 + 50 * i), 110, 'black', 3)
            gui.ellipse((125 + 25 + 50 * i), 110, 6, 6, 'black')
            gui.line((125 + 30 + 50 * i), 135, (125 + 40 + 50 * i), 115, 'black', 3)
            gui.ellipse((125 + 40 + 50 * i), 115, 6, 6, 'black')
            gui.ellipse((125 + 25 + 50 * i), 135, 20, 4, 'black')

        if board[i] == B_KNIGHT:

            # drawing the same "pawn" as white, but in black, for the black knight
            gui.line((125 + 25 + 50 * i), 135, (125 + 25 + 50 * i), 110, 'black', 3)
            gui.ellipse((125 + 25 + 50 * i), 110, 6, 6, 'black')
            gui.ellipse((125 + 25 + 50 * i), 135, 20, 4, 'black')

        i += 1

    gui.update_frame(10)


def is_game_over(board):
    '''

    :param board:
    :return:
    '''

    white_king_found = False
    black_king_found = False

    # iterating through the list to detect a black or white king, if either are found
    # their respective _found variables are turned to true
    i = 0
    while i < 9:
        if board[i] == W_KING:
            white_king_found = True
        if board[i] == B_KING:
            black_king_found = True
        i += 1

    # if both are still there, returns False to "is the game over"
    if black_king_found and white_king_found:
        return False

    # otherwise, if no white king is found, black wins, game over is true
    # also printing the board a final time and printing black wins
    elif not white_king_found:
        print_board(board)
        print('Black wins!')
        return True

    # otherwise, if no black king is found, white wins, game over is true
    # also printing the board a final time and printing white wins
    elif not black_king_found:
        print_board(board)
        print('White wins!')
        return True


def move(board, position, direction):
    '''
    This function calls the appropriate king or knight function based on what
    it detects the character is in that space.
    :param board: should be a list of strings with length of 9
    :param position: should be an integer between 0 and 8 inclusive
    :param direction: should be RIGHT or LEFT
    :return: no return value
    '''
    if board[position] == W_KING or board[position] == B_KING:
        move_king(board, position, direction)
    if board[position] == W_KNIGHT or board[position] == B_KNIGHT:
        move_knight(board, position, direction)


def main():
    
    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]
    
    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE
    
    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:
        
        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)


main()
