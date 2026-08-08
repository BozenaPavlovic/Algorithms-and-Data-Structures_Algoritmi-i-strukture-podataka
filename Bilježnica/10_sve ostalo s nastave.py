#BINARY SEARCH
#%%
def binary_search(arr, target):
    lb = 0
    ub = len(arr)-1
    while lb<=ub:
        mid_idx = (lb + ub) // 2
        mid_val = arr[mid_idx]
        if mid_val == target:
            print('Value %d found at index %d' % (mid_val, mid_idx))
            return mid_idx
        elif mid_val < target:
            lb = mid_idx + 1
        else:
            ub = mid_idx - 1
    print('Value %d not found!' % target)
    return -1

#PRIMJERI REKURZIJE
#%%
def sum_recursive(n):
    if n==1:
        return 1
    else:
        return n + sum_recursive(n-1)

#%%
def sum_loop(n):
    result = 0
    for i in range(n+1):
        result += i
    return result

#%%
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)


#%%
def fact_loop(n):
    if n==0:
        return 1
    else:
        result = 1
        for i in range(n):
            result *= (i+1)
        return result

#%%
def binary_search_recursive(input_list, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        # Ako je traženi element u sredini vraćamo indeks (poziciju)
        if input_list[mid] == target:
            return mid
        elif input_list[mid] > target: # Ako je element manji onda je u lijevom podnizu
            return binary_search_recursive(input_list, low, mid - 1, target)
        else: # Ako je element veći onda je u desnom podnizu
            return binary_search_recursive(input_list, mid + 1, high, target)
    else:
        # Elementa nema u nizu
        return -1

#%%
def hello_world(n):
    for i in range(n):
        print("Hello, World!")

def hello_world_recursive(n):
    if n > 0:
        print("Hello, World!")
        hello_world_recursive(n - 1)

#BROJANJE UČESTALOSTI RIJEČI
#%%
def word_frequency(text):
    word_freq = {}
    words = text.split()

    for word in words:
        if len(word)>0:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq

def custom_word_frequency(text):
    word_freq = CustomDict()
    words = text.split()

    for word in words:
        if len(word)>0:
            if word_freq.contains(word):
                word_freq.set(word, word_freq.get(word) + 1)
            else:
                word_freq.set(word, 1)

    return word_freq



# SPAJANJE RIJEČNIKA 
#%%
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2.keys():
        if key in dict1.keys():
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]

    return result

# Test
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merge_dicts(dict1, dict2)

# MAKSIMALNA VRIJEDNOST
#%%
def find_max(input_dict):
    mx = None
    mx_key = None
    for key, value in input_dict.items():
        if mx is None:
            mx = value
            mx_key = key
        else:
            if value > mx:
                mx = value
                mx_key = key

    return mx_key, mx

test_dict = {'a': 1, 'b': 5, 'c': 7, 'd': 5}
find_max(test_dict)


#BST
#%%
def max_depth(node):
    if not node:
      return 0

    return 1 + max(max_depth(node.left), max_depth(node.right))

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(1)

print("Dubina stabla je:", max_depth(bst.root))  # Očekivano: 4

