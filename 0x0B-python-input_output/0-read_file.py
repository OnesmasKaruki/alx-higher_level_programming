#!/usr/bin/python3
'''Read module'''

def read_file(filename=""):
    """Read text file"""
    with open("filename", 'r',  encoding = "utf-8") as f:
        print(f.read(), end="")