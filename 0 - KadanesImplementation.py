def bruteForce(array):
    globalMaxSum = array[0]

    for i in range(len(array)):
        localMaxSum = 0
        for j in range(j, len(array)):
            localMaxSum += arr[j]
            globalMaxSum = max(globalMaxSum, localMaxSum)

    return globalMaxSum


# EXAMPLE 
# nums = [4, -1, 2, -7, 3, 4]
# print(bruteForce(nums))



def kadanes(array):
    # Initialize maxSum to the first element to handle 
    # the edge case of all negative numbers
    maxSum = array[0]
    # Initialize curSum to 0, representing the sum of the current subarray
    curSum = 0

    # Iterate through each number in the array
    for n in array:
        # Reset curSum to 0 if it becomes negative
        curSum = max(curSum, 0)
        # Add the current number to curSum
        curSum += n
        # Update maxSum if curSum is greater than the current maxSum
        maxSum = max(maxSum, curSum)

    return maxSum


# EXAMPLE 
# nums = [4, -1, 2, -7, 3, 4]
# print(kadanes(nums))


def slidingWindow(array):
    maxSum = array[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(array)):
        if curSum < 0:
            curSum = 0
            L = R
        curSum += array[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 
    return [maxL, maxR]


# EXAMPLE 
# nums = [4, -1, 2, -7, 3, 4]
# print(slidingwindow(nums))