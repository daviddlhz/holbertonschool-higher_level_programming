#!/usr/bin/python3
"""Text indentation
function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with 2 new lines after the characters: .?:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in [".", "?", ":"]:
        if char in text:
            text = text.replace(char, char + "\n\n\a")
    print("\n\n".join([i.strip() for i in text.split("\a")]), end="")
