def reverseList(head):
    # Bazni slučaj: ako je lista prazna ili ima samo jedan element
    if head is None or head.next is None:
        return head

    # Rekurzivno okreni ostatak liste
    new_head = reverseList(head.next)

    # Okretanje pokazivača: neka sljedeći čvor pokazuje natrag na trenutni
    head.next.next = head
    # Prekidamo staru vezu da ne napravimo beskonačnu petlju
    head.next = None

    return new_head