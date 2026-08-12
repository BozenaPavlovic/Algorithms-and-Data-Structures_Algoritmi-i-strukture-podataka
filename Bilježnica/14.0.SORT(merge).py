Merge - Array (top-down)

Singly-linked: pointer-merge (split + merge)

Doubly-linked: pointer-merge (update prev links)


#MERGE SORT 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result += [left[0]]
            left = left[1:]
        else:
            result += [right[0]]
            right = right[1:]

    result += left
    result += right

    return result
  
# MERGE JEDNO
def split_list_single_pointers(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return mid

def merge_single_pointers(left, right):
    if left is None: return right
    if right is None: return left
    if left.data <= right.data:
        result = left
        result.next = merge_single_pointers(left.next, right)
    else:
        result = right
        result.next = merge_single_pointers(left, right.next)
    return result

def merge_sort_single_pointers(head):
    if head is None or head.next is None:
        return head
    mid = split_list_single_pointers(head)
    left_sorted = merge_sort_single_pointers(head)
    right_sorted = merge_sort_single_pointers(mid)
    return merge_single_pointers(left_sorted, right_sorted)
    

# MERGE DOUBLE
def split_list_double_pointers(head):
    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None  # Prekid prednje veze
    if mid is not None:
        mid.prev = None  # 🟢 DODATAK ZA DVOSTRUKU: Prekid stražnje veze
    return mid

def merge_double_pointers(left, right):
    """Spaja dvije sortirane dvostruke liste i obnavlja .prev veze."""
    if left is None: return right
    if right is None: return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_double_pointers(left.next, right)
        if result.next is not None:
            result.next.prev = result  # 🟢 DODATAK ZA DVOSTRUKU (veza unazad)
        result.prev = None
    else:
        result = right
        result.next = merge_double_pointers(left, right.next)
        if result.next is not None:
            result.next.prev = result  # 🟢 DODATAK ZA DVOSTRUKU (veza unazad)
        result.prev = None
    return result

def merge_sort_double_pointers(head):
    if head is None or head.next is None:
        return head
        
    mid = split_list_double_pointers(head)
    
    left_sorted = merge_sort_double_pointers(head)
    right_sorted = merge_sort_double_pointers(mid)
    
    return merge_double_pointers(left_sorted, right_sorted)
