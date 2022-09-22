#!/usr/bin/python3
# islower -> function that checks for lowercase character
# Return -> True ifequal lowercase, otherwise false

def islower(char):
    if (ord(char) > 96 and ord(char) < 123):
        return True
    else:
        False
