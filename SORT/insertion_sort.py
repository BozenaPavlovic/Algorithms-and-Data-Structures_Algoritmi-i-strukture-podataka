def insertion_sort(arr):
    swaps = 0  # brojač zamjena (pomaka)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            swaps += 1  # svaki shift računamo kao zamjenu
            j -= 1

        arr[j + 1] = key
        swaps += 1  # umetanje key-a

    return arr, swaps
