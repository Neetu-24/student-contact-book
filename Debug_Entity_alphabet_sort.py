
def merge_sort(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(M)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    arr = []
    for i in range(len(array)):
        arr.append(array[i])
    return arr

def max_length(a):
    max_length = len(a[0])
    for word in a:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

def equate_lengths(a):
    l = max_length(a)
    for i in range(len(a)):
        if len(a[i]) < l:
            spaces = l - len(a[i])
            a[i] += spaces*" "
    return a

    
def sort_by_index(a, i):
    a = equate_lengths(a)
    x = 0
    d = dict.fromkeys(a,x)
    
    for key in d:
        d[key] = ord(key[i])
    
    list_o = list(d.values())
    order = list(d.values())
    
    for v in range(len(order)):
        order[v] = (v,order[v])

    sorted_arr = []
    b = []
    list_o = merge_sort(list_o)
    
    for s in list_o:
        for j in range(len(order)):
            if order[j][1] == s and j not in b:
                b.append(j)
                break
    for index in b:
        sorted_arr.append(a[index])
    return sorted_arr



def alphabetically_sort(a):
    length = max_length(a)
    
    for i in range(length):
        a = sort_by_index(a,-i-1)
    
    return a






