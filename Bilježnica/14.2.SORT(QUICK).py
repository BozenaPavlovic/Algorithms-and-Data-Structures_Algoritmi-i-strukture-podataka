Array (in-place, Lomuto pivot = arr[high])
Array (functional, pivot = last, left + pivot + right)
SLL (data-swap, pivot = head, swap .data)
SLL (pointer-swap, pivot = head, detach & concat nodes)
DLL (data-swap, pivot = head, swap .data)
DLL (pointer-swap, pivot = head, detach & concat, update .prev/.next)


# QUICK SORT ARR
def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

# QUICK SORT 2 ARR
def quick_sort_2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort_2(left) + [pivot] + quick_sort_2(right)


# QUICK SORT SLL data-swap
def partition_sll_data_swap(head, tail):
    pivot = head
    p = head           # p will mark last node <= pivot after swaps
    curr = head.next   # start from second node

    while curr is not None and curr != tail.next:
        if curr.data < pivot.data:
            p = p.next
            # swap p.data and curr.data
            p.data, curr.data = curr.data, p.data
        curr = curr.next

    # put pivot in its correct place (swap head.data and p.data)
    head.data, p.data = p.data, head.data
    return p

def quick_sort_sll_data_swap_helper(head, tail):
    if head is None or head == tail:
        return

    pivot = partition_sll_data_swap(head, tail)

    # sort left part if exists (need node before pivot)
    if head != pivot:
        prev = head
        while prev.next is not pivot:
            prev = prev.next
        quick_sort_sll_data_swap_helper(head, prev)

    # sort right part
    quick_sort_sll_data_swap_helper(pivot.next, tail)

def quick_sort_sll_data_swap(head):
    if not head:
        return head
    tail = head
    while tail.next:
        tail = tail.next
    quick_sort_sll_data_swap_helper(head, tail)
    return head


# QUICK SORT SLL pointer-swap
def quick_sort_sll_pointer_swap(head):
    if head is None or head.next is None:
        return head

    pivot = head
    curr = head.next
    pivot.next = None

    less_head = less_tail = None
    greater_head = greater_tail = None   # <- was missing

    while curr is not None:
        next_node = curr.next
        curr.next = None
        if curr.data < pivot.data:
            if less_head is None:
                less_head = less_tail = curr
            else:
                less_tail.next = curr
                less_tail = curr
        else:
            if greater_head is None:
                greater_head = greater_tail = curr
            else:
                greater_tail.next = curr
                greater_tail = curr
        curr = next_node

    less_sorted = quick_sort_sll_pointer_swap(less_head)
    greater_sorted = quick_sort_sll_pointer_swap(greater_head)

    # attach pivot after less_sorted (if any)
    if less_sorted is not None:
        new_head = less_sorted
        tail = less_sorted
        while tail.next is not None:
            tail = tail.next
        tail.next = pivot
    else:
        new_head = pivot

    pivot.next = greater_sorted
    return new_head


# QUICK SORT DLL data-swap
def partition_dll_data_swap(head, tail):
    pivot = head
    p = head            # last node <= pivot after swaps
    curr = head.next    # start from second node

    while curr is not None and curr != tail.next:
        if curr.data < pivot.data:
            p = p.next
            p.data, curr.data = curr.data, p.data
        curr = curr.next

    head.data, p.data = p.data, head.data
    return p
def quick_sort_dll_data_swap_helper(head, tail):
    # Provjera valjanosti granica za dvostruku listu
    if head is None or tail is None or head == tail or head == tail.next:
        return
    
    pivot = partition_dll_data_swap(head, tail)

    # Kod DLL-a možemo precizno ići do pivot.prev i od pivot.next
    quick_sort_dll_data_swap_helper(head, pivot.prev)
    quick_sort_dll_data_swap_helper(pivot.next, tail)

def quick_sort_dll_data_swap(head):
    if not head:
        return head
    
    tail = head
    while tail.next:
        tail = tail.next
        
    quick_sort_dll_data_swap_helper(head, tail)
    return head

# QUICK SORT DLL pointer-swap
def quick_sort_dll_pointer_swap(head):
    if head is None or head.next is None:
        return head

    pivot = head
    curr = head.next
    pivot.next = None
    pivot.prev = None

    less_head = less_tail = None
    greater_head = greater_tail = None   # <- fix: initialize both

    while curr is not None:
        next_node = curr.next
        curr.next = None
        curr.prev = None

        if curr.data < pivot.data:
            if less_head is None:
                less_head = less_tail = curr
            else:
                less_tail.next = curr
                curr.prev = less_tail
                less_tail = curr
        else:
            if greater_head is None:
                greater_head = greater_tail = curr
            else:
                greater_tail.next = curr
                curr.prev = greater_tail
                greater_tail = curr
        curr = next_node

    less_sorted = quick_sort_dll_pointer_swap(less_head)
    greater_sorted = quick_sort_dll_pointer_swap(greater_head)

    if less_sorted is not None:
        new_head = less_sorted
        tail = less_sorted
        while tail.next is not None:
            tail = tail.next
        tail.next = pivot
        pivot.prev = tail
    else:
        new_head = pivot

    if greater_sorted is not None:
        pivot.next = greater_sorted
        greater_sorted.prev = pivot

    return new_head
