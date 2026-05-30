def invert_string_keys(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if isinstance(key, str):
            if value not in inverted:
                inverted[value] = [key]
            else:
                inverted[value].append(key)
    return inverted