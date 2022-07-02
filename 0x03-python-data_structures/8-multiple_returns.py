#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if count == 0:
        fest = None
    else:
        fest = sentence[0]
    list_result = []
    list_result.append(count)
    list_result.append(fest)
    tuple_result = tuple(list_result)
    return (tuple_result)
