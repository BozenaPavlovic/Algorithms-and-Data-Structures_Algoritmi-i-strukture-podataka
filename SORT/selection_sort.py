# SELECTION SORT (NIZ / ARRAY – standardna verzija)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# iz primjera s nastave prvi zadatak 
#%%
def find_min(arr):
    mn = arr[0]
    mn_idx = 0
    k = 1
    while k < len(arr):
        if(mn > arr[k]):
            mn = arr[k]
            mn_idx = k
        k += 1
    return mn, mn_idx

def selection_sort(arr):
    for k in range(0,len(arr)-1):
        temp = arr[k]
        mn, mn_idx = find_min(arr[k:len(arr)])
        arr[k] = mn
        arr[k+mn_idx] = temp
    return arr
