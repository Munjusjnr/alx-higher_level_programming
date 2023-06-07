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
    current_line = ""
    lines = []

    for char in text:
        current_line += char
        if char in characters:
            lines.append(current_line.strip())
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    print("\n\n".join(lines))
