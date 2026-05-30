def filter_invert(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if value % 2 == 0:
            if value not in inverted:
                inverted[value] = [key]
            else:
                inverted[value].append(key)
    return inverted