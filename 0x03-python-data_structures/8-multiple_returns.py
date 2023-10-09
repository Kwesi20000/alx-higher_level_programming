#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:  # Check if the sentence is empty
        return (0, None)  # Return a tuple with length 0 and None as the first character
    else:
        return (len(sentence), sentence[0])  # Return a tuple with length and the first character
