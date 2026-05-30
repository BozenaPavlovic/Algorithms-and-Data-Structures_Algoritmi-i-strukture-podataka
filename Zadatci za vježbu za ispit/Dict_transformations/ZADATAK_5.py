def invert_count(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if value not in inverted:
            inverted[value] = 1
        else:
            inverted[value] += 1
    return inverted