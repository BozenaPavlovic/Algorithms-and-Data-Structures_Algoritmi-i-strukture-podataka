def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid  # Broj postoji, vrati indeks
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Ako broj nije pronađen, left je indeks umetanja
    return left