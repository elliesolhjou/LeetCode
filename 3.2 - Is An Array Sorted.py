'''
Write a function that returns a Boolean on whether an array is already sorted in ascending order
'''

def sortedArray (arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False
        
    return True

print(sortedArray([1,3,7,8,-6]))


'''
Write a function that returns:

1 if an array is sorted in ascending order
0 if an array is not sorted 
-1 if an array is sorted in descending order
'''

def sortedArr (arr):
    n = len(arr)
    count=0
    order = 0
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            count+=1
            order-=1
        elif arr[i]<arr[i+1]:
            count+=1
            order+=1
        else:
            count+=1
            order+=0
    # print (count, order)
    if count / order == 1:
        return 1
    elif count / order == -1:
        return -1
    else:
        return 0

        

print(sortedArr([1,2,5,6,7]))
print(sortedArr([1,2,58,7,6,5,4,3,2,6,7]))
print(sortedArr([9,8,7,6,5,4,3,2, 53, 2, 5, 6,7]))