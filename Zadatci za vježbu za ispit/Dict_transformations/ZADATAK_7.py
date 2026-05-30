def invert_sort(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)

    for value in inverted:
        inverted[value].sort()

    return inverted