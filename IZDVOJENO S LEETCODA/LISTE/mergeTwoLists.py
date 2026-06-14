def mergeTwoLists(list1, list2):
    dummy = ListNode()  # Lažni početni čvor
    tail = dummy  # Pokazivač na kraj nove liste

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next  # Pomakni kraj nove liste

    # Ako je u jednoj listi ostalo elemenata, samo ih nadoveži na kraj
    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next  # Vraćamo stvarnu glavu liste (preskačemo dummy)