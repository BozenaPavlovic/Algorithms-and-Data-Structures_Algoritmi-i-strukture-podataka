def nextGreaterElement(nums1, nums2):
    greater_map = {}
    stack = Stack()

    for num in nums2:
        # Dokle god stog nije prazan i trenutni broj je veći od onog na vrhu stoga
        while not stack.is_empty() and num > stack.top():
            popped_num = stack.pop()
            greater_map[popped_num] = num  # Našli smo prvi veći

        stack.push(num)

    result = []
    for num in nums1:
        if num in greater_map:
            result.append(greater_map[num])
        else:
            result.append(-1)

    return result