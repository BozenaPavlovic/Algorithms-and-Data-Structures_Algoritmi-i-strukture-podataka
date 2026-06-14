def maxSubArray(nums):
    # Inicijaliziramo oba zbroja na prvi element (nikako na 0 zbog negativnih brojeva!)
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # Odluči: nastavljaš li stari podniz ili počinješ novi od nums[i]
        current_sum = max(nums[i], current_sum + nums[i])

        # Ažuriraj povijesni maksimum ako je potrebno
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum