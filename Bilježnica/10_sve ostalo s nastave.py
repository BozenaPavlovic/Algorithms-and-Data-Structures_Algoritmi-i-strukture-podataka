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



