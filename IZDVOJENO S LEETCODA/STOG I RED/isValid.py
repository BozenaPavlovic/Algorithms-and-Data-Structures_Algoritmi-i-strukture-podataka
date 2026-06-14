def isValid(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = Stack()  # Koristimo tvoju klasu

    for char in s:
        # Ako je znak zatvorena zagrada
        if char in bracket_map:
            # Ako je stog prazan, a imamo zatvorenu zagradu, niz nije valjan
            if stack.is_empty():
                return False

            top_element = stack.pop()
            # Ako se zagrade ne podudaraju, vraćamo False
            if bracket_map[char] != top_element:
                return False
        else:
            # Ako je otvorena zagrada, stavi je na stog
            stack.push(char)

    # Ako je stog na kraju prazan, sve su zagrade uspješno zatvorene
    return stack.is_empty()