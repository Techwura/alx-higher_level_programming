#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if length > 0:
        first_char = sentence[0]
    else:
        first_char = "None"

    tup = length, first_char
    return tup
