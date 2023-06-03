#!/usr/bin/python3

""" This function print out text after certain characters """


def text_indentation(text):
    """ A function that prints a text then two new lines when meeting
    certain characters

    Parameter:
        text: string to printed out

    Raise:
        TypeError: when the text is not a string

    Return: The text and performing the needed requirements

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [":", ".", "?"]

    words = text.split()

    for i, phrase in enumerate(words):
        print(phrase, end="")
        if any(char in phrase for char in characters):
            print("\n")
        elif i < len(words) - 1:
            print(" ", end="")
