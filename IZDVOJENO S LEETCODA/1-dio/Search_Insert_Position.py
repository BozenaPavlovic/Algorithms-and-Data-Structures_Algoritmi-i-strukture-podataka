def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Pronalazimo sredinu niza

        if nums[mid] == target:
            return mid  # Target pronađen, vraćamo njegov indeks
        elif nums[mid] < target:
            left = mid + 1  # Target je veći, tražimo desno
        else:
            right = mid - 1  # Target je manji, tražimo lijevo

    # Ako broj nije pronađen, 'left' će na kraju petlje
    # točno pokazivati na indeks gdje bi broj trebao biti umetnut.
    return left