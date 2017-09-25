"""This module is for a program that manipulates a string based on
- If the letter in string is upper case letter, replace that letter
  with a string containing every letter from A to that letter.For example,
  if the input letter is H , then the output would be ABCDEFGH.
- If the letter in string is lower case letter, replace that letter
  with a string containing every letter from a to that letter.
  For example, if the input letter is h , then the output would be abcdefgh.
- If letter in string is number(0-9), replace that letter with a string
  containing numbers from 0 to that number. For example, if input letter is 3,
  then the output would be 0123 .
- All other characters are printed without modification.
https://www.hackerearth.com/problem/golf/modify-string/
"""
import string
from random import randint


def modify_string(word):
    """The main function for manipulating the string"""
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    numbers_0_to_9 = [ str(x) for x in range(0, 10) ]
    output = ''
    all_lists = [uppercase_letters, lowercase_letters, numbers_0_to_9]
    
    for letter in word:
        char_exists = False
        for every_list in all_lists:
            position = binary_search(letter, every_list)
            if position is not None:
                char_exists = True
                output += create_word_till_char(letter, position, every_list) 
        if not char_exists:
            output += letter
    return output

def binary_search(character, list_of_characters, position=0):
    """Searches for character using binary seacrh"""
    length_of_list = len(list_of_characters)
    if length_of_list <= 1:
        if length_of_list == 0:
            return None
        if character != list_of_characters[0]:
            return None
        return position

    random_int = randint(0, length_of_list - 1)
    if character < list_of_characters[random_int]:
        new_list = list_of_characters[:(random_int)]
        position += 0
    else:
        new_list = list_of_characters[random_int:]
        position += random_int
    # return this so that it recursively comes back to the surface
    return binary_search(character, new_list, position)


def create_word_till_char(character, position, list_of_characters):
    """Create word from a list till a given position"""    
    if not list_of_characters or position is None:
        return ''
    sliced_list = list_of_characters[: position + 1]
    return ''.join(sliced_list)


if __name__ == '__main__':
    print(modify_string(input()))
