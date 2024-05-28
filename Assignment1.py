# dsa course
'''
1. (10 points) Write an example for each of the following. 
Avoid using examples that were already discussed in class. Examples do not necessarily have to be programming related:

O(1)
O(log n)
O(n)
O(n log n)
O(n2)

'''

# O(1)
nums = [1, 2, 3,4 , 5, 5, 6, 7]
lastNum = nums.pop()

# o(log n) binary search
def guess(arr, target):
    # define pointers
    L, R = 0, len(arr)-1

    # define search space
    while L <= R:
        mid = (L+R)//2
        if target > arr[mid]:
            L = mid+1
        elif target < arr[mid]:
            R = mid-1
        else:
            return mid
    
    return -1


# O(n)
nums = [1, 2, 3,4 , 5, 5, 6, 7]
def doubleNums(nums):
    for n in nums:
        return n*2

# O(n log n) - Any sorting Algo (Heap Sort)
import heapq
nums = [1, 2, 3,4 , 5, 5, 6, 7]

# o(n)
heapq.heapify(nums)
while nums:
    # o(logn)
    heapq.heappop(nums)



nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# O(n2) - Traverse a square grid
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print (nums[i][j])

# O(n2) - Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        print((nums[i], nums[j]))

'''
2. (20 points) Write code to populate an array with the size n with numbers from 0 to n-1. 
Afterwards, shuffle (randomly reorder or rearrange)  the numbers in the array.
Do not use any built-in functions such as shuffle(). However, feel free to use the 
built-in random() function.

Examples:

[0, 1, 2, 3] -> shuffled: [2, 0, 3, 1]
[0, 1, 2, 3, 4, 5] -> shuffled: [5, 2, 4, 1, 3, 0]
And finally, provide the Big O notation for both the average and worst case 
time complexities of your code.
'''
import random

def createArray(n):
    orderedArray = list(range(n))
    # swap index
    randIndex = random.randint(0, n-1)
    for i in range(n):
        # swap
        orderedArray[i], orderedArray[randIndex] = orderedArray[randIndex], orderedArray[i]
        
    return orderedArray
# print(createArray(6))


'''
3. (35 points) Write a function that accepts a sorted array of integers and
 a target value. The array may contain duplicate values. It should return the 
 count of the number of occurrences of the target value.

Examples:

[0, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5] Target: 3, should return 6
[1, 1, 2, 3, 3, 4, 5, 5, 5] Target: 5, should return 5
[1, 1, 2, 3, 3, 4, 5, 5, 5] Target: 6, should return 0
Full credit for a O(log n) solution and partial credit otherwise.


 o(n)
    count = 0
    for n in array:
        if n == target:
            count+=1
    return count
'''
# find the containing window
# O(log n) - binary search

def find_first_position(arrayOne, target):
    L, R = 0, len(arrayOne) - 1
    while L <= R:
        mid = (L + R) // 2
        print(f"in firs rep and R index is {R} and array[mid] is {arrayOne[mid]}")
        if arrayOne[mid] <= target:
            L = mid + 1
        else:
            R = mid - 1
    return (L-1)
def find_last_position(arrayOne, target):
    L, R = 0, len(arrayOne) - 1
    while L <= R:
        mid = (L + R) // 2
        # it finds the last rep on left (bc of =)
        # by shifting pointers to left till it stuck on last rep
        if arrayOne[mid] >= target:
            R = mid - 1
        else:
            L = mid + 1

    return (R+1)

def occur(arrayOne, target):
    a = find_first_position(arrayOne, target)
    b = find_last_position(arrayOne, target)
    if a>b:
        return a-b+1
    else:
        return b-a+1

print(occur([0, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5], 3))

# print(find_first_position([0, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5], 3))
# print(find_last_position([0, 1, 2,  , 3, 3, 3, 3, 3, 4, 4, 5], 3))


'''
4. (35 points) Write a function that accepts a sorted,
rotated array and returns the index of the largest value. 
Assume that the array is sorted in ascending order.

A rotated array is an array that has had its elements shifted or 
rotated circularly to the left or right by a certain number of positions. 
This rotation does not change the elements themselves but changes their 
positions within the array.

Examples:
[1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3] # max value index: 1 (value: 5)
[0, 1, 3, 5, 7, 11] -> [5, 7, 11, 0, 1, 3] # max value index: 2 (value: 11)

# o(n)
def largeNumIndex(array):
    maxNum = 0
    index = 0
    for i in range(len(array)):
        if array[i]>maxNum:
            maxNum = array[i]
            index = i
        else:
            pass
    return index

print(largeNumIndex([5, 7, 11, 0, 1, 3]))

Full credit for a O(log n) solution and partial credit otherwise.

'''
# o(log n) -> binary search
#  if rep -> find L and R index by = ing target and pointers
def find_max_index(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1
    return right