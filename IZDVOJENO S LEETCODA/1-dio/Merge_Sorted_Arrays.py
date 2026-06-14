def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Postavljamo pokazivače na krajeve oba niza
    p1 = m - 1  # Zadnji stvarni element u nums1
    p2 = n - 1  # Zadnji element u nums2
    p = m + n - 1  # Zadnja pozicija u nums1 (gdje upisujemo)

    # Dokle god imamo elemenata u oba niza za usporedbu
    while p1 >= 0 and p2 >= 0:
        # Uspoređujemo koji je element veći i stavljamo ga na kraj
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1  # Pomičemo pokazivač za upis jedno mjesto ulijevo

    # Ako su u nums2 ostali elementi (jer su manji od svih preostalih u nums1),
    # samo ih prebacimo na preostala prazna mjesta na početku nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1