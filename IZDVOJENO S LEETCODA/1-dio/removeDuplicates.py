def removeDuplicates(nums):
    if not nums:
        return 0

    # Prvi element je uvijek jedinstven, pa upis kreće od indeksa 1
    write_index = 1

    for read_index in range(1, len(nums)):
        # Ako je trenutni broj različit od prethodnog, imamo novi jedinstveni broj
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1  # Pomakni mjesto za idući upis

    return write_index  # Vraća broj jedinstvenih elemenata