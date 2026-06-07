def find_max(input_dict):
    mx = None
    mx_key = None
    for key, value in input_dict.items():
        if mx is None:
            mx = value
            mx_key = key
        else:
            if value > mx:
                mx = value
                mx_key = key

    return mx_key, mx

test_dict = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
find_max(test_dict)




# Maksimalna vrijednost
# Napišite funkciju `find_max` koja će pronaći maksimalnu vrijednost u riječniku, korištenjem `dict` metode `.items()`.
# Trebat ćete koristi *for* petlju, ali u kojoj je iterator par ključ-vrijednost, jer metoda `.items()` vraća ključ-vrijednost parove.



def find_min(input_dict):
    mn = None
    mn_key = None
    
    for key, value in input_dict.items():
        if mn is None:
            mn = value
            mn_key = key
        else:
            if value < mn:  # Tražimo manju vrijednost
                mn = value
                mn_key = key

    return mn_key, mn
