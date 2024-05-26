# insertion sort implementation

# O(n^2)
# best case is ordered array and O(n) - while loop not executed
def insertionSort(arr):
    for i in range(len(arr)):
        j = i-1
        while j > 0 and arr[j+1]<arr[j]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j-=1

# recursive binary sort
# o(nlogn)
# memory complexity O(n)
def mergeSort(arr, s, e):
    s, e = 0, len(arr)-1
    # R-L+1 is length of array
    # base case
    if e-s+1<=1:
        # we reached base case of on element array which 
        # is already sorted
        return arr
    mid = (s+e)//2
    # binary sort
    # subproblems
    mergeSort(arr, s, mid)
    mergeSort(arr, mid+1, e)
    # mergin subproblems
    merge(arr, s, e)

    return arr

# Merge in-place
def merge(arr, s, m, e):
    # Copy the sorted left & right halfs to temp arrays
    L = arr[s:m+1]
    R = arr[m+1:e+1]

    # define pointers to do comparison and positioning
    i = 0
    j = 0
    k = s 
    # k is pointer for main array that would returned at the end
    while i < len(L) and j< len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            k+=1
            i+=1
        else:
            arr[k]= R[j]
            k+=1
            j+=1
        # k+=1

        # one of the halves have more
        # element than the other so for remaining
        while i<len(L):
            arr[k] = L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k] = R[j]
            k+=1
            i+=1
