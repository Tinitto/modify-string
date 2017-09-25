import string

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
            if letter in every_list:
                char_exists = True
                output += create_word_till_char(letter, every_list.index(letter), every_list) 
        if not char_exists:
            output += letter
    return output

def create_word_till_char(character, position, list_of_characters):
    """Create word from a list till a given position"""    
    if not list_of_characters or position is None:
        return ''
    sliced_list = list_of_characters[: position + 1]
    return ''.join(sliced_list)


if __name__ == '__main__':
    print(modify_string(input()))
    