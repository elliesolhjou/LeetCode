'''

Describe the worst case data and the best case data for each of the following sorting algorithms.
Also, include the big O notation for each case.
Bubble Sort

Selection Sort
Insertion Sort
Merge Sort
Quicksort
'''


'''Implement an insertion sort function.'''

def insertionSort (arr):
    for i in range(len(arr)):
        j = i-1
        while j>=0 and arr[j+1]<arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            # tmp = arr[j]
            # arr[j] = arr[j+1]
            # arr[j+1] = tmp
            j-=1
    return arr

print(insertionSort([2,4,62,1,5,7,12]))

'''
Write a function that accepts an array and 
returns an array of numbers missing from it
The input array:
has a size n
contains random numbers ranging from 0 to n-1
may contain duplicate values
not necessarily sorted
The output array:
contains missing numbers ranging from 0 to n-1.
This function must have a time complexity of O(n) to get full credit.

For example:
Given the array [0, 3, 6, 7, 3, 3, 0, 4], this function should return [ 1, 2, 5 ]

'''
def missedNum(arr):
    # O(n^2)
    missed=[]
    n = len(arr)
    arr.sort()          
    for i in range(1,n):
        diff = 0
        if arr[i]-arr[i-1]>1:
            diff = arr[i]-arr[i-1]
            for j in range(1,diff):
                missed.append(arr[i]-j)
    return missed

# O(n)
def missedNumber(arr):
    n= len(arr)
    missed=[]
    max_size= max(arr)
    presence = [False] * (max_size+1)
    for num in arr:
        print(f"number is {num}")
        # print (num)
        presence[num] = True
    for i in range(len(presence)):
        if presence[i] == False: 
            missed.append(i)
    return missed

# arr = [1,2,3,8,3,7,0]
arr = [0, 3, 6, 7, 3, 3, 0, 4]
# arr.sort()
# print(missedNum(arr))
print(missedNumber(arr))

''''
4. Write a function that returns the first 
non-repeating character in a string with O(n) efficiency. 
It should return none or null if there are no non-repeating 
conesutive characters.

For example:

string "aaaaabbbbbbc", this function should return "c"
string "aabab" should return "b"  
string "aababb" should return  None ("b" is repeating)
'''

def repFunc(string):
    # define a set to see if it was presented and try to keep elements of it unique
    # if a char is repeated consecutively (check with repeat char set)-> we remove it from hash set
    hset = set()
    # define a set to add consecutives number
    repeat_char = set()

    # prev pointer to check with for consecutiveness
    prev = None

    for ch in string:
        # if character was never seen before and not repeated -> it is present and unique
        if ch not in hset and ch not in repeat_char:
            # add char to the presented char sets
            hset.add(ch)
        
        # if char was presented before and it is consecutive
        # add to repeatchar_set -> we don't like it so we remove
        elif ch in hset and ch==prev:
            hset.remove(ch)
            repeat_char.add(ch)
        prev = ch
    
    for c in string:
        if c in hset:
            return c

    return None






# print(repFunc("aababb"))




def repFinderChar(str):
    # for unique chars
    unique_char= set()
    # for consec chars
    repeated_char= set()
    prev = None
    for c in str:
        if c not in unique_char and c not in repeated_char:
            unique_char.add(c)
        elif c in unique_char and c== prev:
            repeated_char.add(c)
            unique_char.remove(c)
        prev = c
    # print(unique_char)
    # print(repeated_char)
    for c in str:
        if c in unique_char:
            return c

print(repFinderChar("aaaaabbbbbbcc"))


'''
5. Write a function that given an array of integers and a 
target value, returns the length of the longest subarray with a sum equal 
to the target value. Write the function with O(n) efficiency for full credit.

Note: while the sliding window technique is acceptable as a solution, 
try solving this using a hash table.

For example:
Given an array [3, 1,-1, 2, -1, 5, -2, 3] and a target value of 3,
the longest subarray length is 5 ([-1, 2, -1, 5, -2])
'''


def largeSum(arr, target):
    max_length=0
    for  i in range(len(arr)): 
        cur_sum = arr[i]
        for j in range(i+1, len(arr)):
            cur_sum+=arr[j]
            if cur_sum == target:
                max_length = max(max_length, j-i+1)
    
    return max_length

print(largeSum([3, 1, -1, 2, -1, 5, -2, 3], 4))
            

                


    

    # max(len(subarray))
    # sum(subarray) = target
    # return len(subarray)

