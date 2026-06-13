def binary_search_recursive(input_list, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        # Ako je traženi element u sredini vraćamo indeks (poziciju)
        if input_list[mid] == target:
            return mid
        elif input_list[mid] > target: # Ako je element manji onda je u lijevom podnizu
            return binary_search_recursive(input_list, low, mid - 1, target)
        else: # Ako je element veći onda je u desnom podnizu
            return binary_search_recursive(input_list, mid + 1, high, target)
    else:
        # Elementa nema u nizu
        return -1
