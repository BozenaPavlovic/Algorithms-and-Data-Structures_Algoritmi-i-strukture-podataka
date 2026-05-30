def invert_dict_unique(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if value in inverted:
            raise ValueError(f"Duplikat vrijednosti: {value}")
        inverted[value] = key
    return inverted