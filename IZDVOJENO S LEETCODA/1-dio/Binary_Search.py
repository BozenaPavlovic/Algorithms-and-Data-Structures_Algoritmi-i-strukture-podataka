def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Cjelobrojno dijeljenje (traženje sredine)

        if nums[mid] == target:
            return mid  # Target pronađen, vrati njegov indeks
        elif nums[mid] < target:
            left = mid + 1  # Target je veći, odbaci lijevu polovicu niza
        else:
            right = mid - 1  # Target je manji, odbaci desnu polovicu niza

    return -1  # Ako petlja završi, traženi broj ne postoji u nizu