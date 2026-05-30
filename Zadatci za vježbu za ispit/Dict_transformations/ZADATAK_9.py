def invert_if(dictionary, condition):
    inverted = {}
    for key, value in dictionary.items():
        if condition(value):
            if value not in inverted:
                inverted[value] = [key]
            else:
                inverted[value].append(key)
    return inverted