# Napišite funkciju invert_dict koja prima rječnik (Python dict) kao argument i 
# vraća novi rječnik s obrnutim ključevima i vrijednostima. Ako su vrijednosti u originalnom rječniku 
# nejedinstvene, svaka vrijednost treba odgovarati listi originalnih ključeva. 
# >>> invert_dict({'a': 1, 'b': 2, 'c': 1}) 
# => {1: ['a', 'c'], 2: ['b']} 



def invert_dict(dictionary):
    inverted = {}
    for key, value in dictionary.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted


