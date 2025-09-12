#!/usr/bin/python3

"""
prints a text with 2 new lines after each of these characters: ., ? and :
text: text to print
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = ""
    i = 0
    while i < len(text):
        if text[i] in [".", "?", ":"]:
            new_text += text[i] + "\n\n"
            if text[i + 1] == " ":
                i += 1
        else:
            new_text += text[i]
        i += 1
    print(new_text, end="")
