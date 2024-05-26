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


