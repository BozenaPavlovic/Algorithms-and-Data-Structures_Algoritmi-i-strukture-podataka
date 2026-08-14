ARR
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

# Singly-linked: data swap
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def bucket_sort(self, bucket_count):
        if self.head is None or self.head.next is None or bucket_count < 1:
            return

        # 1. min i max
        cur = self.head
        min_val = max_val = cur.data
        while cur:
            if cur.data < min_val: min_val = cur.data
            if cur.data > max_val: max_val = cur.data
            cur = cur.next
        if min_val == max_val:
            return

        # 2. kreiraj buckete (heads)
        buckets = [None] * bucket_count

        # 3. raspodijeli čvorove (push-front)
        cur = self.head
        while cur:
            nxt = cur.next
            idx = int((cur.data - min_val) * bucket_count / (max_val - min_val))
            if idx < 0: idx = 0
            if idx >= bucket_count: idx = bucket_count - 1
            cur.next = buckets[idx]
            buckets[idx] = cur
            cur = nxt

        # helper: insertion sort by data-swap za singly list (ascending)
        def insertion_sort_data_swap(head):
            if head is None or head.next is None:
                return head
            current = head.next
            while current:
                key = current.data
                node = head
                while node is not current:
                    if node.data > key:
                        node.data, key = key, node.data
                    node = node.next
                current.data = key
                current = current.next
            return head

        # 4. sort svaki bucket (data-swap)
        for i in range(bucket_count):
            if buckets[i] is not None:
                buckets[i] = insertion_sort_data_swap(buckets[i])

        # 5. konkateniraj buckete
        new_head = None
        new_tail = None
        for i in range(bucket_count):
            b = buckets[i]
            if b is None: continue
            if new_head is None:
                new_head = b
            else:
                new_tail.next = b
            # pomakni tail do kraja bucketa
            t = b
            while t.next:
                t = t.next
            new_tail = t

        self.head = new_head
        
# Doubly-linked: data swap
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def bucket_sort(self, bucket_count):
        if self.head is None or self.head.next is None or bucket_count < 1:
            return

        # 1. min i max
        cur = self.head
        min_val = max_val = cur.data
        while cur:
            if cur.data < min_val: min_val = cur.data
            if cur.data > max_val: max_val = cur.data
            cur = cur.next
        if min_val == max_val:
            return

        # 2. bucketi (head samo, koristimo push-front radi jednostavnosti)
        buckets = [None] * bucket_count

        # 3. raspodijeli čvorove (detach i push-front)
        cur = self.head
        while cur:
            nxt = cur.next
            cur.prev = None
            cur.next = None
            idx = int((cur.data - min_val) * bucket_count / (max_val - min_val))
            if idx < 0: idx = 0
            if idx >= bucket_count: idx = bucket_count - 1
            head = buckets[idx]
            if head is None:
                buckets[idx] = cur
            else:
                cur.next = head
                head.prev = cur
                buckets[idx] = cur
            cur = nxt

        # helper: insertion sort by data-swap za doubly list (ascending)
        def insertion_sort_data_swap_doubly(head):
            if head is None or head.next is None:
                return head
            current = head.next
            while current:
                j = current
                while j.prev and j.prev.data > j.data:
                    j.prev.data, j.data = j.data, j.prev.data
                    j = j.prev
                current = current.next
            return head

        # 4. sort svaki bucket
        for i in range(bucket_count):
            if buckets[i] is not None:
                buckets[i] = insertion_sort_data_swap_doubly(buckets[i])

        # 5. konkateniraj buckete (postavi prev/next ispravno)
        new_head = None
        new_tail = None
        for i in range(bucket_count):
            b = buckets[i]
            if b is None: continue
            if new_head is None:
                new_head = b
                # pronađi tail bucketa
                t = b
                while t.next:
                    t = t.next
                new_tail = t
            else:
                # spoj tail -> b
                new_tail.next = b
                b.prev = new_tail
                t = b
                while t.next:
                    t = t.next
                new_tail = t

        self.head = new_head
