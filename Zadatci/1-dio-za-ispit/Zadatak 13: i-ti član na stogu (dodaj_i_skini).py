# ==============================================================================
# ZADATAK 13: i-ti član na stogu bez uništavanja stoga
#
# TEKST ZADATKA:
# Napišite funkciju koja vraća i-ti član na stogu iz klase Stog (i=0 označava 
# vrh stoga). Stog nakon izlaska iz funkcije mora ostati nepromijenjen, 
# a smiju se koristiti samo osnovne metode za rad sa stogovima: dodaj ( push ) i skini ( pop ).
# ==============================================================================

def get_stack_i_th_element(stack, i):
    temp_stack = Stack()
    result = None
    index = 0

    # pop elements until we reach i-th
    while not stack.is_empty():
        value = stack.pop()

        if index == i:
            result = value

        temp_stack.push(value)
        index += 1

    # restore original stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return result
