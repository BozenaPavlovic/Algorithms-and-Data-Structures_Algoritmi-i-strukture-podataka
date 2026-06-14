def reverseString(s):
    def helper(left, right):
        # Bazni slučaj: kada se pokazivači susretnu ili mimoiđu
        if left >= right:
            return

        # Zamijeni znakove na pozicijama left i right
        s[left], s[right] = s[right], s[left]

        # Rekurzivni poziv za unutrašnji dio niza
        helper(left + 1, right - 1)

    # Pokrećemo rekurziju s početnim indeksima
    helper(0, len(s) - 1)