def invert_append(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        new_key = f"key_{value}"
        if new_key not in inverted:
            inverted[new_key] = [key]
        else:
            inverted[new_key].append(key)
    return inverted