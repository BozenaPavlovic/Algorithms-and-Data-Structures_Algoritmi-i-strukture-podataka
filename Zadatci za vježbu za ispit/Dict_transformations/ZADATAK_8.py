def merge_invert(dict1, dict2):
    inverted = {}

    for d in [dict1, dict2]:
        for key, value in d.items():
            if value not in inverted:
                inverted[value] = [key]
            else:
                inverted[value].append(key)

    return inverted