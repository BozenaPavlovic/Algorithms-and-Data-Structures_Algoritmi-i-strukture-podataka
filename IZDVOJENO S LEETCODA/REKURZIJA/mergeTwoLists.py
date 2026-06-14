def mergeTwoLists(list1, list2):
    # Bazni slučajevi: ako je jedna od lista prazna, vrati onu drugu
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Rekurzivni korak: spajamo manji element s ostatkom
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2