def print_upper_words(word_list):
    """Take every word in the list and prints all in uppercase

    Args:
        word_list (list): list of all words to be converted to uppercase
    """
    
    for word in word_list:
        print(word.upper())
       
def print_upper_words2(word_list):
    """Take every word in the list and prints, in uppercase, all the ones that start with "e" or "E" 
        >>> print_upper_words2(["hello", "hey", "goodbye", "yo", "yes","elephant"])    
        ....
        elephant
    
    """
    for word in word_list:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())
        

def print_upper_words3( word_list, must_start_with):
    """Take every word in the list and prints the ones that start with the letters in the 2nd arg in uppercase

        >>> print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
            .....
            HELLO
            HEY
            YO
            YES     

    """
    for word in word_list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes","elephant"])    
print_upper_words2(["hello", "hey", "goodbye", "yo", "yes","elephant"])    
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})