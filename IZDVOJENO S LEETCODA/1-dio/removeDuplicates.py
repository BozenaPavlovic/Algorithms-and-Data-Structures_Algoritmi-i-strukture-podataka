def removeDuplicates(nums: list[int]) -> int:
    # Ako je niz prazan, ima 0 jedinstvenih elemenata
    if not nums:
        return 0

    # Pokazivač koji označava mjesto gdje upisujemo sljedeći jedinstveni element
    # Prvi element (na indeksu 0) je uvijek jedinstven, pa krećemo od indeksa 1
    write_index = 1

    # Prolazimo kroz niz s 'read_index' počevši od drugog elementa
    for read_index in range(1, len(nums)):
        # Ako je trenutni element različit od onog ispred njega, pronašli smo novi jedinstveni broj!
        if nums[read_index] != nums[read_index - 1]:
            # Upisujemo ga na poziciju write_index
            nums[write_index] = nums[read_index]
            # Pomičemo pokazivač za upis jedno mjesto udesno
            write_index += 1

    # Broj jedinstvenih elemenata (k) je točno jednak poziciji write_index
    return write_index