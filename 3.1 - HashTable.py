'''
Write a function that accepts an array and returns the most frequently appearing value.

'''
countMap={"ali":2}
print(countMap["ali"])
import math
def highCount(arr):
    countMap={}
    for data in arr:
        # cant't find
        # if countMap[data] !=0:
        if data in countMap:
            countMap[data] +=1
        else:
            countMap[data] = 1

    maxCount = 0
    freqKey= None
    for key, val in countMap.items():
        if val>maxCount:
            print(key, val)
            maxCount = val
            freqKey = key

    return freqKey


print(highCount([2,1,1,1,1,1,3,4,4,4,4,4,4,4,4,4,4,4,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))


'''
A given array is filled with unsorted numbers from 0 to n. 
There is exactly one number missing in this array.
Write an efficient function to find this missing number.
'''

a = [2,1,1,1,1,1,3,4,4]
a.sort()
print(a)

def missingNum (arr):
    n = len(arr)
    if n<=1:
        raise IndexError ("not enough length")
    arr.sort()
    for i in range(n):
        if arr[i+1]-arr[i]>1:
            return arr[i]+1
        
print(missingNum([9,6,7,3,4,5,2,1]))

#most efficient way:
def missedNum(arr):
    n = len(arr)+1
    # i missed number
    perfectSum = n*(n+1)//2
    print(perfectSum)
    actualSum = sum(arr)
    print(actualSum)
    return (perfectSum-actualSum)
print(missedNum([7,3,4,5,2,1]))