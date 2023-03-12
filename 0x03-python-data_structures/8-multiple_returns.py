#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)

    if sentence == "":
        return sen_len, None
    else:
        return sen_len, sentence[0]
