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
    return arr

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

# advantage of quick sort over merge sort -> happens in place less memory complexity

# Quick sort O(n^2)
# pivotal sort -> pick a value and compare other element to pivot
# height of tree is n in worstcase (ordered array) 

#  1. take a pivot (usually last element)
#  2. define two pointers
    #  one to help us iterate through array
    #  onr to show the position the order element should be placed
#  3. partiotning (smaller than pivot on left), after iteration pointer reaches pivot element
#  4. swap position pointer value with pivot value 
#  5. make recursive calls on left and right side 

def quickSort(arr, s, e):
    # define base case
    if e-s+1<=1:
        return arr
    
    # define pivot
    # assign a value
    pivot = arr[e]

    # define pointers
    positionPointer = s
    # i as second pointer for iteration

    # partitioning: smaller than  pivot move to positionPointer
    # don't count pivot in iteration - range takes care of it
    for i in range(s, e):
        # swap
        if arr[i]<= pivot:
            # tmp = arr[positionPointer]
            # arr[positionPointer] = arr[i]
            # arr[i] = tmp
            arr[positionPointer], arr[i] = arr[i], arr[positionPointer]
            positionPointer +=1

    '''  not updating pivot -pivot is a value an integer not a pointer to the actual memory cell 
    This line does not correctly place the pivot into the array because it assigns 
    the value of pivot to the variable pivot, but it does not update the array.
    You should directly swap the pivot element with the element at positionPointer in the array.
    arr[positionPointer] , pivot = pivot , arr[positionPointer]
    '''
    # Swap/Move last element (AKA pivot) to correct location
    arr[positionPointer], arr[e] = arr[e], arr[positionPointer]

    # recursive call on left side (smaller than pivot)
    # position pointer is at right place
    quickSort(arr, s, positionPointer-1)

    # recursive call on left side (smaller than pivot)
    quickSort(arr, positionPointer+1, e)

    return arr
    # since it is all happening in place no need to merge

# unordered_array = [10, 7, 8, 9, 1, 5, 3, 6, 2, 4]
unordered_array = [1,3,59,8,3,6,2,7,9]
fc = quickSort(unordered_array, 0, len(unordered_array)-1)
print(fc)



# selection sort - O(n ^ 2)
# find minimum element and swap with i element where we are at ith iteration
def selectionSort (arr):
    # define two pointers
        # one pointer to iterate (i)
        # one pointer to find minimum val between arr[i] and rest of array (arr-arr[:i])
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                # before index J is sorted so move pointer
                # 
                min_index = j
        # when found min val index at each subarray iteration then swap it with arr[i]
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



# Bubble Sort
# in iteration when first no swap happens, pointer moves to next element
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr