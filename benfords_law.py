# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program prompts the user for a file name (works for .txt and .csv),
#                   and a mode for displaying the UI, either 'text' or 'gui', and processes
#                   the file to determine if the dataset follows Benford's Law, which states 
#                   that natural datasets' numbers' leading values skew toward lower values (1)
#                   compared to higher values (9). Useful for detecting fraud or non-natural 
#                   data sets.

from graphics import graphics

def user_input():
    """
    This function prompts the user for the filename and mode, and returns the
    mode and a list version of the read file.
    return: read_file_list should be a list of strings based on the original csv
    return: input_mode should be a string, either 'text' or 'gui'
    """
    input_file_name = input('Data file name:\n')
    input_mode = input('Mode:\n')
    # added this so when we do gui, we don't have an extra newline in console
    if input_mode == 'text':
        print()
    read_file = open(input_file_name, 'r')
    read_file_list = read_file.readlines()
    read_file.close()
    return read_file_list, input_mode

def convert_to_number_list(read_file_list):
    """
    This function takes the read_file_list and converts it 
    to a number list by splitting on the commas, and appending
    the values to a number list based on certain conditions.   
    param: read_file_list should be a list of strings
    return: number_list should be a list of float values
    """
    number_list = []

    for line in read_file_list:
        strip_line = line.rstrip()
        split_list = strip_line.split(',')

        for element in split_list:
            #identifying first character
            f_char = str(element[0])
            #identifying last character
            l_char = str(element[(len(element)-1)])

            # if the first character isn't 0, and is numeric, and if the last character is numeric
            # need to say !='0' because !=0 would be saying "if the character exists"
            if f_char.isnumeric() and f_char != '0' and l_char.isnumeric():
                # if the element's characters pass the logic check, then we append it to the number list
                number_list.append(float(element))

    return number_list

def process_number_list(number_list):
    """
    This function takes a list of numbers and determines the breakdown of percentages for 
    the numbers' leading digits, and determines if its following Benford's law
    param: number_list should be a list of floats
    return: percentage dictionary should be a dictionary with keys between 1-9, and integer values<=100
    return: follow_law should be a boolean
    """
    follow_law = True
    # counter_dictionary who's values will increase
    counter_dictionary = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    # "perfect outcome" benford dictionary to compare the percentages to
    benford_dictionary = {1:30, 2:17, 3:12, 4:9, 5:7, 6:6, 7:5, 8:5, 9:4}
    # creating a percentage dictionary based off of the percentages calculated, used for displaying charts
    percentage_dictionary = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    # increasing the values of the counter dictionary by 1 for each matching number in number list
    for number in number_list:
        counter_number = int((str(number))[0])
        counter_dictionary[counter_number] += 1

    # calculating relative percentage of numbers occuring in counter_dictionary and storing
    # percentages in percentage_dictionary
    for key in counter_dictionary:
        percentage = (counter_dictionary[key]/len(number_list))*100
        percentage_dictionary[key] = percentage

        # using "perfect" benford_dictionary to compare percentages. if any are out of
        # scope, then doesn't follow law. otherwise, stays true
        if not benford_dictionary[key]-5 <= percentage <= benford_dictionary[key]+10:
            follow_law = False

    return percentage_dictionary, follow_law

def display_text_version(percentage_dictionary, follow_law):
    """
    This function displays the text version of the graph based on the
    percentage_dictionary and if the law was followed.
    param: percentage_dictionary should be a dictionary with keys 1-9 and integer values
    param: follow_law should be a boolean
    """
    for key in percentage_dictionary:
        # printing the key, and # symbols based on the value in the dictionary
        print(str(key) + ' | ' + "#"*int(percentage_dictionary[key]))

    if follow_law:
        print("\nFollows Benford's Law")
    else:
        print("\nDoes not follow Benford's Law")
    
def display_gui_version(percentage_dictionary, follow_law):
    """
    This function displays the GUI version of the result charts based on the 
    percentage dictionary and if the dataset follows Benford's law. 
    param: percentage_dictionary should be a dictionary with keys 1-9 and integer values
    param: follow_law should be a boolean
    """
    #drawing the canvas and white background
    gui = graphics(500, 500, "Benford's Law")
    gui.rectangle(0,0,500,500, 'white')

    #drawing the axis lines
    gui.line(44, 40, 44, 410, 'black', 1)
    gui.line(30, 400, 470, 400, 'black', 1)

    # drawing the title, and also a legend for the axes
    gui.text(150, 20, "Benford's Law Analysis Results:", 'black', 12)
    gui.text(44, 430, 'y-axis = leading digit of a number', 'black', 8)
    gui.text(44, 440, 'x-axis = percentage frequency of occurance in data set', 'black', 8)
    
    # drawing the follow/does not follow message based on the boolean, changes colors
    if follow_law:
        gui.text(225, 460, "Follows Benford's Law", 'green', 13)
    else:
        gui.text(225, 460, "Does not follow Benford's Law", 'red', 13)

    # iterating through the percentage dictionary to draw the chart
    for key in percentage_dictionary:
        # drawing the y axis numbers based on the key we're on
        gui.text(25, 50 + 40*(int(key)-1), str(key), 'black', 15)

        # drawing the bars based on the value at each key
        i = 0
        while i < int(percentage_dictionary[key]):
            gui.rectangle(45 + 10*i, 58 + 40*(int(key)-1), 10, 10, 'red')
            i += 1

    # drawing the x-axis tick marks, and number labels 
    i = 0
    while i < 43:

        # for every 5 tick marks, making the tick red, and displaying the multiple of 5
        if i % 5 == 0 and i != 0:
            gui.line(54 + 10*(i-1), 405, 54 + 10*(i-1), 395, 'red', 1)

            # if the multiple of 5 is 2-digits long, then it gets off center of the tick
            # mark, so i have this conditional logic
            if i >= 10:
                gui.text(38 + 10*i, 408, str(i), 'black', 8)
            else:
                gui.text(41 + 10*i, 408, str(i), 'black', 8)
        
        # if the tick mark isn't a multiple of 5, its just a regular tick mark
        else:
            gui.line(54 + 10*(i-1), 405, 54 + 10*(i-1), 395, 'black', 1)
        i += 1

    gui.draw()

def main():

    # calling the user input function and getting a read_file_list and mode
    read_file_list, input_mode = user_input()
    #converting the list to a more usable number list
    number_list = convert_to_number_list(read_file_list)
    #processing the number list to calculate the percentages for each #, and if the law is followed
    percentage_dictionary, follow_law = process_number_list(number_list)

    #displaying the text or gui version based on original input mode
    if input_mode == 'text':
        display_text_version(percentage_dictionary, follow_law)
    if input_mode == 'gui':
        display_gui_version(percentage_dictionary, follow_law)

main()
