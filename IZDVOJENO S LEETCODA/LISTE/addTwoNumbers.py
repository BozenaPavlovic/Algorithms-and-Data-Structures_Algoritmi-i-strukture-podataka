def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0  # Varijabla za prijenos (0 ili 1)

    # Petlja radi dok god ima elemenata u l1 ILI l2 ILI imamo preostali prijenos
    while l1 is not None or l2 is not None or carry > 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        # Izračunaj zbroj i novi prijenos
        total = val1 + val2 + carry
        carry = total // 10  # Cjelobrojno dijeljenje daje prijenos
        digit = total % 10  # Ostatak daje novu znamenku

        # Stvori novi čvor s izračunatom znamenkom
        curr.next = ListNode(digit)
        curr = curr.next

        # Pomakni liste na sljedeći čvor ako postoje
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return dummy.next