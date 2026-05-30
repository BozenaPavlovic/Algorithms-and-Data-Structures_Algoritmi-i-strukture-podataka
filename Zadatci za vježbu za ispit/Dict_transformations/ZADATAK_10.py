from collections import defaultdict

def invert_defaultdict(dictionary):
    inverted = defaultdict(list)
    for key, value in dictionary.items():
        inverted[value].append(key)
    return dict(inverted)