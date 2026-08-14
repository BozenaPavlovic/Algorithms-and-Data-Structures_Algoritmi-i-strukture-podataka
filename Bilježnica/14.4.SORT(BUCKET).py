ARR
Singly-linked: pointer
Doubly-linked: pointer
Singly-linked: data swap
Doubly-linked: data swap


# BUCKET SORT ARR
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Put array elements in different buckets
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    # Sort individual buckets using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate all buckets into arr[]
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

# -------------------------
# Helpers for linked-list bucket variants
# -------------------------
def _flatten_sll_to_array(head, out_arr, start_index=0):
    cur = head
    i = start_index
    while cur:
        out_arr[i] = cur.data
        i += 1
        cur = cur.next
    return i  # next index

def _flatten_dll_to_array(head, out_arr, start_index=0):
    cur = head
    i = start_index
    while cur:
        out_arr[i] = cur.data
        i += 1
        cur = cur.next
    return i


# -------------------------
# simple insertion sorts for linked buckets (used internally)
# -------------------------
def insertion_sort_single_data(head):
    if head is None or head.next is None:
        return head
    cur = head.next
    while cur:
        start = head
        while start is not cur:
            if start.data > cur.data:
                start.data, cur.data = cur.data, start.data
            start = start.next
        cur = cur.next
    return head

def insertion_sort_single_pointers(head):
    if head is None or head.next is None:
        return head
    sorted_head = None
    cur = head
    while cur:
        nxt = cur.next
        # insert into sorted_head
        if sorted_head is None or cur.data <= sorted_head.data:
            cur.next = sorted_head
            sorted_head = cur
        else:
            p = sorted_head
            while p.next and p.next.data < cur.data:
                p = p.next
            cur.next = p.next
            p.next = cur
        cur = nxt
    return sorted_head

def insertion_sort_double_data(head):
    if head is None or head.next is None:
        return head
    cur = head.next
    while cur:
        start = head
        while start is not cur:
            if start.data > cur.data:
                start.data, cur.data = cur.data, start.data
            start = start.next
        cur = cur.next
    return head

def insertion_sort_double_pointers(head):
    # build sorted DLL by detaching and inserting nodes
    if head is None or head.next is None:
        return head
    sorted_head = None
    cur = head
    while cur:
        nxt = cur.next
        cur.prev = cur.next = None
        if sorted_head is None or cur.data <= sorted_head.data:
            cur.next = sorted_head
            if sorted_head:
                sorted_head.prev = cur
            sorted_head = cur
        else:
            p = sorted_head
            while p.next and p.next.data < cur.data:
                p = p.next
            cur.next = p.next
            cur.prev = p
            p.next = cur
            if cur.next:
                cur.next.prev = cur
        cur = nxt
    return sorted_head


# -------------------------
# 2) BUCKET SORT - SLL using pointer-based buckets (store nodes; sort by pointer)
# -------------------------
def bucket_sort_sll_pointer(arr, bucket_count=None):
    n = len(arr)
    if n == 0:
        return arr
    if bucket_count is None:
        bucket_count = n

    heads = [None] * bucket_count
    tails = [None] * bucket_count

    # distribute into SLL buckets (append to tail)
    for num in arr:
        bi = int(bucket_count * num)
        if bi >= bucket_count:
            bi = bucket_count - 1
        node = Node(num)
        if heads[bi] is None:
            heads[bi] = tails[bi] = node
        else:
            tails[bi].next = node
            tails[bi] = node

    # sort each bucket (pointer insertion) and flatten back into arr
    idx = 0
    for i in range(bucket_count):
        heads[i] = insertion_sort_single_pointers(heads[i])
        if heads[i] is not None:
            idx = _flatten_sll_to_array(heads[i], arr, idx)
    return arr


# -------------------------
# 3) BUCKET SORT - SLL using data-swap inside buckets (build lists, sort by data-swap)
# -------------------------
def bucket_sort_sll_data(arr, bucket_count=None):
    n = len(arr)
    if n == 0:
        return arr
    if bucket_count is None:
        bucket_count = n

    heads = [None] * bucket_count
    tails = [None] * bucket_count

    # distribute
    for num in arr:
        bi = int(bucket_count * num)
        if bi >= bucket_count:
            bi = bucket_count - 1
        node = Node(num)
        if heads[bi] is None:
            heads[bi] = tails[bi] = node
        else:
            tails[bi].next = node
            tails[bi] = node

    # sort each bucket by swapping data inside nodes, then flatten
    idx = 0
    for i in range(bucket_count):
        heads[i] = insertion_sort_single_data(heads[i])
        if heads[i] is not None:
            idx = _flatten_sll_to_array(heads[i], arr, idx)
    return arr


# -------------------------
# 4) BUCKET SORT - DLL using pointer buckets (maintain prev/next; pointer-insert sort)
# -------------------------
def bucket_sort_dll_pointer(arr, bucket_count=None):
    n = len(arr)
    if n == 0:
        return arr
    if bucket_count is None:
        bucket_count = n

    heads = [None] * bucket_count
    tails = [None] * bucket_count

    # distribute (append to tail)
    for num in arr:
        bi = int(bucket_count * num)
        if bi >= bucket_count:
            bi = bucket_count - 1
        node = DoublyNode(num)
        if heads[bi] is None:
            heads[bi] = tails[bi] = node
        else:
            tails[bi].next = node
            node.prev = tails[bi]
            tails[bi] = node

    # sort each bucket (pointer insertion for DLL) and flatten
    idx = 0
    for i in range(bucket_count):
        heads[i] = insertion_sort_double_pointers(heads[i])
        if heads[i] is not None:
            idx = _flatten_dll_to_array(heads[i], arr, idx)
    return arr


# -------------------------
# 5) BUCKET SORT - DLL using data-swap inside buckets
# -------------------------
def bucket_sort_dll_data(arr, bucket_count=None):
    n = len(arr)
    if n == 0:
        return arr
    if bucket_count is None:
        bucket_count = n

    heads = [None] * bucket_count
    tails = [None] * bucket_count

    # distribute
    for num in arr:
        bi = int(bucket_count * num)
        if bi >= bucket_count:
            bi = bucket_count - 1
        node = DoublyNode(num)
        if heads[bi] is None:
            heads[bi] = tails[bi] = node
        else:
            tails[bi].next = node
            node.prev = tails[bi]
            tails[bi] = node

    # sort each bucket (data-swap) and flatten
    idx = 0
    for i in range(bucket_count):
        heads[i] = insertion_sort_double_data(heads[i])
        if heads[i] is not None:
            idx = _flatten_dll_to_array(heads[i], arr, idx)
    return arr
