def merge(nums1, m, nums2, n):
    # Postavljanje pokazivača na krajeve
    p1 = m - 1  # Zadnji stvarni element u nums1
    p2 = n - 1  # Zadnji element u nums2
    p = m + n - 1  # Zadnja pozicija u nums1 (mjesto za upis)

    # Spajaj elemente dok god ima brojeva u oba niza
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Ako su u nums2 ostali manji elementi, samo ih prebaci na početak nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1