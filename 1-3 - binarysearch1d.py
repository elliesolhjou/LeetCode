'''
This question has two parts.

Write code to generate a random number. Make the number range as large as possible.
Write code to automatically guess the number from part A. Your code is aware of the range from part A.
'''
import math
import random


# create a range of nums in array
rangeNum = list(range(-9999999, 9999999))
def randomNum():
    target = random.randint(rangeNum[0], rangeNum[-1])
    # print(target)
    return target

randomNum()

def guess(arr):

    target = randomNum()
    print (f"generated random target is {target}")

    # define left and write pointers
    L , R = 0, len(arr)-1

    # define valid search space 
    while L <= R:
        mid = (L+R)//2
        if target> arr[mid]:
            # move pointers
            L = mid+1
        elif target < arr[mid]:
            # move pointers
            R = mid-1
        else:
            # found the target
            print(F"Found Target")
            return arr[mid]

    # target not found at all and L is > R  search space is NONE
    return -1


print(guess(rangeNum))

    
    


    

'''
Modify the previous section so that it will guess the number, 
but the code is not aware of the range in part A. 

'''

# Optional chatgpt 
def randomNum():
    # Generate a random number within a very large range
    min_val = -2**63
    max_val = 2**63 - 1
    return random.randint(min_val, max_val)

def guess():
    target = randomNum()
    print(f"Generated random target is {target}")

    # Initial guess boundaries
    L, R = -1, 1
    
    # Expand the range exponentially until the target is within range
    while target < L or target > R:
        L, R = L * 2, R * 2
        if L > target or R < target:  # In case L or R overflow beyond the target
            L, R = min(L, target), max(R, target)
    
    # Perform binary search within the determined range
    attempts = 0
    while L <= R:
        attempts += 1
        mid = L + (R - L) // 2
        if target > mid:
            L = mid + 1
        elif target < mid:
            R = mid - 1
        else:
            print(f"Found Target in {attempts} attempts")
            return mid

    return -1  # Target not found (this should not happen in this context)

print(guess())

