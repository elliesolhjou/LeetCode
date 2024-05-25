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
print(createArray(6))







    # print (randNum(5))
    # for i in range (n):
    #     if randNum in orgArray:
    #         randNum(n)
            
    #     # orgArray[randNum(n)] = i

    # return orgArray

# print(createArray(10))