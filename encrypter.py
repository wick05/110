# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program is used in tandem with decrypter.py. You give it the name of a .txt file,
#                   and it creates encrypted key and content .txt files


import random


def process_file(filename):
    """
    processes .txt file to encrypt. creates a list
    based on the file, returns the line count, list
    :param filename: this should be a string of the users inputted .txt file to encrypt
    :return: returns an integer line_count, and a list
    """
    file = open(filename, 'r')
    list_read_file = file.readlines()
    file.close()
    line_count = len(list_read_file)

    # strips newlines from elements in the list
    i = 0
    while i < len(list_read_file):
        list_read_file[i] = list_read_file[i].rstrip('\n')
        i += 1
    return line_count, list_read_file


def create_encrypt_key_list(line_count):
    """
    takes the line count of the file to encrypt,
    creates a list
    function contains the core encryption algorithm
    :param line_count: should be an integer
    :return: returns a list
    """
    # creating a stock index list through the length of the user's file
    index_list = [0] * line_count
    #  1-based instead of 0 based ([1,2,3,4,5,6,7,8,9,10])
    for i in range(line_count):
        index_list[i] = i + 1

    # core encryption algorithm, creating 2 random index numbers, and swapping the values at those indexes
    i = 0
    while i < line_count*5:
        random_number1 = random.randint(0, line_count-1)
        random_number2 = random.randint(0, line_count-1)

        # creating a temporary container to help with swapping
        temp_value = index_list[random_number1]
        index_list[random_number1] = index_list[random_number2]
        index_list[random_number2] = temp_value
        i += 1

    return index_list


def create_index_file(index_list):
    """
    takes the list of the key/index and writes it to a file
    :param index_list: should be a list
    :return: void
    """
    index_file = open('index.txt', 'w')
    i = 0 
    while i < len(index_list):
        # exception where we don't want a newline on the last line
        if i == len(index_list) - 1:
            index_file.write(str(index_list[i]))
        else:
            index_file.write(str(index_list[i]) + '\n')
        i += 1
    index_file.close()


def scramble_og_file(index_list, readfile_list):
    """
    uses  encryption index/key  with list version of the
    user's file, writes out the encrypted contents file.
    :param index_list:
    :param readfile_list:
    :return:
    """
    # creating temporary/encrypted list based on encryption/index list and original file contents
    encrypt_list = []
    i = 0
    while i < len(readfile_list):
        # taking the value of the index/key list - 1, using that value
        # as a readfile index for appending lines to encrypt list
        index_to_scramble = int(index_list[i]) - 1
        encrypt_list.append(readfile_list[index_to_scramble])
        i += 1

    # writing the temporary/encrypted list to a file
    file = open('encrypted.txt', 'w')
    i = 0
    while i < len(encrypt_list):
        file.write(str(encrypt_list[i]) + '\n')
        i += 1
    file.close()


def main():
    random.seed(125)

    file_name = input('Enter a name of a text file to encrypt:\n')
    line_count, readfile_list = process_file(file_name)
    index_key_list = create_encrypt_key_list(line_count)
    create_index_file(index_key_list)
    scramble_og_file(index_key_list, readfile_list)


main()
