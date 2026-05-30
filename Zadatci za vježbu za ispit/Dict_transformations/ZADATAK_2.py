def invert_dict_set(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if value not in inverted:
            inverted[value] = {key}
        else:
            inverted[value].add(key)
    return inverted