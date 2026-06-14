def subsets(nums):
    result = []

    def backtrack(index, current_subset):
        # Bazni slučaj: prošli smo sve elemente, spremi kopiju u rezultat
        if index == len(nums):
            result.append(list(current_subset))  # list() radi obaveznu kopiju
            return

        # Odluka 1: Uključi trenutni broj u podskup
        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)

        # Backtrack korak: izbaci ga van da bismo probali drugu odluku
        current_subset.pop()

        # Odluka 2: Preskoči trenutni broj
        backtrack(index + 1, current_subset)

    # Pokrećemo algoritam s indeksom 0 i praznom listom
    backtrack(0, [])
    return result