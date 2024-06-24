from typing import List

'''
Kadane Algorithm: 
used for subarray problems for questions such as maximum subarray, minimum subarray
this can be an alternative to traditional sliding window technique

this builds on the fact that the subarray at each pass would be either itself, or the localised maximum subarray

Optimised Time Complexity: O(n)
Optimised Space Complexity: O(1)
'''
# determine the maximum subarray using kadane's algorithm
# this is a greedy approach since this would choose the best decision and compare it with the local amxima
def maxSubArray(nums: List[int]) -> int:
    globalMax, localMax = nums[0], nums[0]
    for r in range(1, len(nums)):
        localMax = max(nums[r], localMax + nums[r])
        if localMax > globalMax:
            globalMax = localMax
    return globalMax

