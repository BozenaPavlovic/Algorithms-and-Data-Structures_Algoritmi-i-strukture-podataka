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
