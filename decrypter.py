# Author:           Jake Wick
# Course:           CSc 110
# Description:      This program is used in tandem with encrypter.py. Tell it the name of the index "key"
#                   file and the name of the encrypted file, and it will decrypt it.


def process_index_file(user_input_index_filename):
    """
    This function opens an index/key file and converts it to a list
    :param user_input_index_filename: should be a string of the users input
    :return: a list version of the index file
    """
    read_index_file = open(user_input_index_filename, 'r')
    index_list = read_index_file.readlines()
    read_index_file.close()
    return index_list


def descramble(filename, index_list):
    """
    This function takes the users input of the encrypted filename, and the index list, and ultimately
    writes a decrypted version of the encrypted file.
    :param filename: should be a string of the users input
    :param index_list: should be a list
    :return: void
    """
    # opening the encrypted file and capturing as list
    read_encrypted_file = open(filename, 'r')
    encrypted_list = read_encrypted_file.readlines()
    read_encrypted_file.close()

    # removing the newlines from the encrypted list elements
    i = 0
    while i < len(encrypted_list):
        encrypted_list[i] = encrypted_list[i].rstrip('\n')
        i += 1

    temp_list = []

    # the most logic intensive section, this area appends to the temporary list based on the
    # index key
    i = 0
    # for every element in the encrypted list
    while i < len(encrypted_list):
        j = 0
        # iterating through the index/key list, and if the numerical value of the index/key
        # matches the current encrypt index + 1 (because the key is not 0 based),
        # then we append the encrypted list's value
        while j < len(index_list):
            if int(index_list[j]) == i + 1:
                temp_list.append(encrypted_list[j])
            j += 1
        i += 1

    # writing the temporary list to the decrypted file
    decrypted_file = open('decrypted.txt', 'w')
    i = 0
    while i < len(temp_list):
        if i == (len(temp_list) - 1):
            decrypted_file.write(str(temp_list[i]))
        else:
            decrypted_file.write(str(temp_list[i]) + '\n')
        i += 1
    decrypted_file.close()


def main():
    # prompting the user for the filenames, which in all cases are pretty much going to be
    # encrypted.txt and index.txt
    user_input_encrypted_filename = input('Enter the name of an encrypted text file:\n')
    user_input_index_filename = input('Enter the name of the encryption index file:\n')

    # capturing a list based on the index key
    index_list = process_index_file(user_input_index_filename)

    descramble(user_input_encrypted_filename, index_list)


main()
