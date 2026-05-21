def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2.keys():
        if key in dict1.keys():
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]

    return result

# Test
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merge_dicts(dict1, dict2)


# Spajanje rječnika
# Napišite funkciju koja spaja dva rječnika, ali tako da se vrijednosti s istim ključevima zbrajaju.

# Točan ispis u testnom primjeru ispod bi trebao biti:
# {'a': 1, 'b': 5, 'c': 7, 'd': 5}
