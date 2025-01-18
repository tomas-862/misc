import random

def shuffle_words():
    # Ask the user to input a list of words separated by spaces
    user_input = input("Enter a list of words separated by spaces: ")
    
    # Split the input string into a list of words
    words = user_input.split()
    
    # Shuffle the list of words randomly
    random.shuffle(words)
    
    # Print the shuffled list of words in a single line
    print("Shuffled words:", ' '.join(words))

shuffle_words()