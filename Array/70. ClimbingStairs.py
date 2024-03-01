'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''
# Recursive Approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    

# Non Recursive Approach
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         stack=[]
#         for i in range(n+1):
#             if i<=2:
#                 stack.append(i)
#                 print("i is ", i, stack)
#             else:
#                 stack.append(stack[-1]+stack[-2])
#         return stack[-1]

sol = Solution()
result = sol.climbStairs(5)
print(result)

