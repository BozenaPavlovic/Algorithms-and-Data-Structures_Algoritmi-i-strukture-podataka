# Normalno (niz / array)

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1] # zamjena elemenata
                swapped = True
        if not swapped:
            break
    return arr
