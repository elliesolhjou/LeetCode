'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

'''

class Solution:
    def quickSort(self, arr):
        if arr:
            s= 0
            e= len(arr)-1
            print(f"e is {e}")
            pivot= arr[e]
            print(f" pivot is {pivot}")
            left= s
            if (e-s)+1<=1:
                return arr
            else:
                for i in range(e+1):
                    print(f"i is {i}")
                    if arr[i]<=pivot:
                        print (f"true, arr[i]{arr[i]} is smaller than pivot {pivot} and positioning pointer is at {left}")
                        temp = arr[left]
                        arr[left]=arr[i]
                        arr[i]= temp
                        left += 1
                        print(f"new left is at {left}")
                        print (f'new arr is {arr}')
                    arr[e] = arr[left]
                    arr[left] = pivot
            self.quickSort(arr[:left-1])
            self.quickSort(arr[left+1:])

        return arr

    def findKthLargest(self, nums, k):
        sortedArr = (self.quickSort(nums))
        print(sortedArr)
        return sortedArr[k]
    


sol= Solution()
result = sol.findKthLargest([3,2,4,5,5,3],4)  
print(result)           
