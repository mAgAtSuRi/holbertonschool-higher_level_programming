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
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            new_text += text[i] + "\n\n"
        else:
            new_text += text[i]
    print(new_text)
text_indentation('f', 'erer')