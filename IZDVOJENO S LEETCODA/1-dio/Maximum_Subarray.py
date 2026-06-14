def maxSubArray(nums: list[int]) -> int:
    # Na početku, i trenutni i maksimalni zbroj postavljamo na prvi element
    current_sum = nums[0]
    max_sum = nums[0]

    # Prolazimo kroz ostatak niza (od indeksa 1 nadalje)
    for i in range(1, len(nums)):
        # Odlučujemo: isplati li se nastaviti stari podniz ili uzeti samo trenutni broj?
        current_sum = max(nums[i], current_sum + nums[i])

        # Ako je trenutni zbroj postao veći od povijesnog maksimuma, ažuriramo max_sum
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum