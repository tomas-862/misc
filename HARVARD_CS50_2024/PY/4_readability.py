
# Write, in a file called readability.py in a folder called sentimental-readability, a program that first asks the user to type in some text,
# and then outputs the grade level for the text, according to the Coleman-Liau formula.

# Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text,
# and S is the average number of sentences per 100 words in the text.

# Use get_string from the CS50 Library to get the user’s input, and print to output your answer.

# Your program should count the number of letters, words, and sentences in the text.
# You may assume that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word,
# and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.

# Your program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
# If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level),
# your program should output "Grade 16+" instead of giving the exact index number. If the index number is less than 1, your program should output "Before Grade 1".


# readability.py in the sentimental-readability folder

from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = 0
    words = 0
    sentences = 0

    # Count letters, words, and sentences
    for char in text:
        if char.isalpha():  # Count letters
            letters += 1
        if char.isspace() or char in ('.', '!', '?'):  # Count words and sentences
            if char.isspace():  # Word boundary
                words += 1
            if char in ('.', '!', '?'):  # End of a sentence
                sentences += 1

    # Counting the last word if text doesn't end with space
    words += 1 if text and text[-1] != ' ' else 0  # Increment words for last word

    # Calculate L and S
    L = (letters / words) * 100  # Average letters per 100 words
    S = (sentences / words) * 100  # Average sentences per 100 words

    # Coleman-Liau index formula
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Determine the output grade level
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
    
