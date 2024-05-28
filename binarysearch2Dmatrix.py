'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool`
        """
        for matrice in matrix:
            L, R = 0, len(matrice)-1
            while L <= R:
                mid = (L+R)// 2
                if target> matrice[mid]:
                    L= mid+1
                elif target<matrice[mid]:
                    R = mid-1
                else:
                    return True
        # this return should be one level out to enable while loop goes to the second row, 
        # otherwise it just iterates over one row
        return False