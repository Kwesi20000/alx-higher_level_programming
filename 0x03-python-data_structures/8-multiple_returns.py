#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:  # Check if the sentence is empty
        return (0, None)  # Return a tuple with length and character
    else:
        return (len(sentence), sentence[0])
