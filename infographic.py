# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program receives a user's .txt file and gives a breakdown
#                   of the average length of words, most common words of each size, 
#                   capitalization, and punctuation.
from graphics import graphics

def user_input():
    """
    reads the user's file into a list of strings, and returns
    the filename and list.
    return: read_file_list is a list of strings based off file
    return: input_file_name is a string of the filename
    """
    input_file_name = input('Data file name:\n')

    read_file = open(input_file_name, 'r')
    read_file_list = read_file.readlines()
    read_file.close()
    return read_file_list, input_file_name

def convert_to_words_list(read_file_list):
    """
    converts the list of strings to a list of
    all words in file
    return: all words list is a list of strings
    """
    all_words_list = []

    # converting the read file list into a list of words
    for string in read_file_list:
        stripped_string = string.rstrip('\n')
        split_list_of_string = stripped_string.split()
        for word in split_list_of_string:
            all_words_list.append(word)

    return all_words_list

def convert_to_dict(words_list):
    """
    converts all of the words to a dictionary
    with counts
    return: dictionary of words is a dictionary of words   
    """
    dictionary_of_words = {}
    #converting the list of words to a dictionary of words with counts
    for word in words_list:
        if word not in dictionary_of_words:
            dictionary_of_words[word] = 1
        else:
            dictionary_of_words[word] += 1

    return dictionary_of_words
    
def most_common_word(dictionary_of_words):
    """
    iterates through dictionary to find the most common
    word of each length type (small, med, large)
    param: dictionary_of_words is a dict of word(string):frequency(int)
    return: sml_dictionary is a 3 length dictionary word(string):frequency(int)
    """
    s_m_l_dictionary = {}

    #floor variables for comparing str frequency
    small_floor = 0
    medium_floor = 0
    large_floor = 0

    small_word = ''
    medium_word = ''
    large_word = ''


    for key in dictionary_of_words:
        # if small
        if len(key) <= 4:   
            # comparing current word frequency, storing word and frequency
            if dictionary_of_words[key] > small_floor:
                small_floor = int(dictionary_of_words[key])
                small_word = key
        #med
        elif 5 <= len(key) <= 7:
            if dictionary_of_words[key] > medium_floor:
                medium_floor = int(dictionary_of_words[key])
                medium_word = key
        #large
        else:
            if dictionary_of_words[key] > large_floor:
                large_floor = int(dictionary_of_words[key])
                large_word = key

    #adding words as keys and frequency as value in dictionary
    s_m_l_dictionary[small_word] = small_floor
    s_m_l_dictionary[medium_word] = medium_floor
    s_m_l_dictionary[large_word] = large_floor

    return s_m_l_dictionary

def counting_unique_capitalized(dictionary_of_words):
    """
    iterating through dictionary keys(unique words)
    to see if capitalized or not, returning the counts and the 
    amount of unique words
    param: dictionary_of_words is a dict of word(string):frequency(int)
    return: uppercase_counter, lowercase_counter are integers
            (the combined amount is the amount of unique words)
    """
    uppercase_counter = 0
    lowercase_counter = 0
    
    for key in dictionary_of_words:
        if key[0].isupper():
            uppercase_counter += 1
        else:
            lowercase_counter += 1

    return uppercase_counter, lowercase_counter, uppercase_counter+lowercase_counter

def counting_unique_punct(dictionary_of_words):
    """ 
    iterating through dictionary of words (unique words),
    counting how many are punctuated or not
    param: dictionary_of_words is a dict of word(string):frequency(int)
    return: punct_counter, nonpunct_counter are integers
    """
    punct_counter = 0
    nonpunct_counter = 0
    
    for key in dictionary_of_words:
        if key[-1] in {'.', ',', '?', '!'}:
            punct_counter += 1
        else:
            nonpunct_counter += 1

    return punct_counter, nonpunct_counter

def unique_words_sml_dict(dictionary_of_words):
    """
    this function creates a 3 length dictionary of counts of unique words
    of each length type
    param: dictionary_of_words is a dict of word(string):frequency(int)
    return: unique_words_sml_dict is a 3 length dictionary sizecategory(string):frequency(int)
    """
    unique_words_sml_dict = {'small':0, 'med':0, 'large':0}

    # iterating through dictionary of unique words, and adding to the counter
    # of their length categories
    for key in dictionary_of_words:
        if len(key) < 5:
            unique_words_sml_dict['small'] += 1
        elif 5 <= len(key) <= 7:
            unique_words_sml_dict['med'] += 1
        else:
            unique_words_sml_dict['large'] += 1

    return unique_words_sml_dict

def calc_pixel_heights(unique_words_dict, upper, lower, punct, nonpunct):
    """
    This function takes previously calculated values/counts and 
    calculates the pixel proportions they should take for the 3 graphs.
    param: unique_words_sml_dict is a 3 length dictionary sizecategory(string):frequency(int)    
    param: upper, lower, punct, nonpunct are integers
    return: pix_list is a list of integers representing how much height certain values should take up
    """
    
    total_unique_item_count = 0
    #list of the values of occurences of small, medium, and large words
    sml_list = []

    for key in unique_words_dict:
        total_unique_item_count += int(unique_words_dict[key])
        sml_list.append(int(unique_words_dict[key]))

    #NEEDS TO BE UNIQUE WORDS...
    small_pix_y = (450/total_unique_item_count) * int(sml_list[0])
    med_pix_y = (450/total_unique_item_count) * int(sml_list[1])
    lrg_pix_y = (450/total_unique_item_count) * int(sml_list[2])

    upp_pix_y = (450/(upper+lower)) * upper
    low_pix_y = (450/(upper+lower)) * lower

    punc_pix_y = (450/(punct+nonpunct)) * punct
    npunc_pix_y = (450/(punct+nonpunct)) * nonpunct
    
    pix_list = [small_pix_y, med_pix_y, lrg_pix_y, upp_pix_y, low_pix_y, punc_pix_y, npunc_pix_y]

    return pix_list

def display_gui(pixel_list, sml_dictionary, file_name, total_unique_words):
    """
    this function uses the pixel list to display the 3 charts, the sml dictionary to display the most 
    common word of each length category, and displays the filename, total unique words
    param: pixel_list is a list of integers representing how much height certain values should take up
    param: sml_dictionary is a 3 length dictionary word(string):frequency(int)
    param: filename is a string
    param: total_unique_words is an integer
    """
    # pixel list reference = [small_pix_y, med_pix_y, lrg_pix_y, upp_pix_y, low_pix_y, punc_pix_y, npunc_pix_y]

    #window
    gui = graphics(650, 700, 'Infographic (barbenheimer)')
    #background
    gui.rectangle(0,0,650,700, 'white')

    #file name, total unique words, and header for most common word(s)
    gui.text(275, 25, file_name, 'black', 15)
    gui.text(218, 75, 'Total Unique Words:   ' + str(total_unique_words), 'orange', 10)
    gui.text(100, 100, 'Most used words (small, medium, large): ', 'black', 10)
    
    #most common words, printing them in a column using a pixel offset in y axis
    word_offset = 0
    for key in sml_dictionary:
        gui.text(350, 100+ word_offset, key + ' (' + str(sml_dictionary[key]) + 'x)', 'black', 10)
        word_offset += 25

    #chart for relative amount of unique words of each size category
    #small
    gui.rectangle(125, 200, 100, pixel_list[0], 'deeppink1')
    #med
    gui.rectangle(125, 200 + pixel_list[0], 100, pixel_list[1], 'deeppink2')
    #large
    gui.rectangle(125, 200 + pixel_list[0] + pixel_list[1], 100, pixel_list[2], 'deeppink3')
    gui.text(128, 665, 'total unique', 'black', 8)
    gui.text(128, 675, 'sml, med, lrg words', 'black', 8)

    #chart for relative amount of uppercase and lowercase unique words
    #uppercase 
    gui.rectangle(275, 200, 100, pixel_list[3], 'mistyrose3')
    #lowercase 
    gui.rectangle(275, 200 + pixel_list[3], 100, pixel_list[4], 'mistyrose4')
    gui.text(275, 675, 'upper/lowercase words', 'black', 8)

    #chart for relative amount of punctuated and nonpunctuated words
    #punct
    gui.rectangle(425, 200, 100, pixel_list[5], 'mistyrose4')
    #nonpunct
    gui.rectangle(425, 200 + pixel_list[5], 100, pixel_list[6], 'mistyrose3')
    gui.text(425, 675, 'punct/nonpunctuated words', 'black', 8)

    gui.draw()

def main():
    
    #getting filename from user and storing contents in a list
    read_file_list, file_name = user_input()

    # converting the list of contents to a words list, then a dictionary of unique words/counts
    words_list = convert_to_words_list(read_file_list)
    dictionary_of_words = convert_to_dict(words_list)

    #using the dictionary of unique words to find most common word of each size category
    mostcommon_word_dict = most_common_word(dictionary_of_words)

    #using the dictionary of words to get counts for unique words
    upper_counter, lower_counter, total_unique_words = counting_unique_capitalized(dictionary_of_words)
    punct_counter, nonpunct_counter = counting_unique_punct(dictionary_of_words)
    unique_words_sml_category_list = unique_words_sml_dict(dictionary_of_words)

    #calculating pixels for unique word charts
    pix_list = calc_pixel_heights(unique_words_sml_category_list, upper_counter, lower_counter, punct_counter, nonpunct_counter)

    #displaying 3 charts, most common word (x3), filename, total unique words
    display_gui(pix_list, mostcommon_word_dict, file_name, total_unique_words)

main()