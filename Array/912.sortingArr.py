'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

'''

# class Solution:
#     def sortArray(self, nums):
#         for i, num in enumerate(nums):
#             j= i-1
#             while j>= 0 and nums[j+1]<= nums[j]:
#                 print (f"j is {j} and i is {i}")
#                 print(f" nums before : {nums}")
#                 temp = nums[j+1]
#                 nums[j+1] = nums[j]
#                 nums[j] = temp
#                 print (f" nums after: {nums}")
#                 print (f" nums[i] after: {nums[i]}")
#                 j -= 1
#                 print (f"j after: {j}")
#         return nums

# DO NOT PUT I INSTEAD OF J+1 -> IF YOU PUT I -> THE POINTER WOULD NOT MOVE IN CORRELATION WITH J
    # very inefficient -> Time Limit Exceeded (TLE)
        



class Solution:
    def sortArray(self, nums):
        newArr= [nums[0]]
        nums.pop(0)
        for i in nums:
            if i <= newArr[0]:
                newArr.insert(0, i)
                print (newArr)
            elif i >= newArr[-1]:
                newArr.append(i)
            # else:

                



sol = Solution()
result = sol.sortArray([5,2,3,1])
print(result)