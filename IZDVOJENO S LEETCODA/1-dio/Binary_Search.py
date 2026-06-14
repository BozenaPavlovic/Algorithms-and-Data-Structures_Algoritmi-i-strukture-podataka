def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Cjelobrojno dijeljenje za indeks sredine

        if nums[mid] == target:
            return mid  # Broj je pronađen, vrati indeks
        elif nums[mid] < target:
            left = mid + 1  # Target je veći, traži u desnoj polovici
        else:
            right = mid - 1  # Target je manji, traži u lijevoj polovici

    return -1  # Broj ne postoji u nizu