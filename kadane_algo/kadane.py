'''
Kadane Algorithm: 
used for subarray problems for questions such as maximum subarray, minimum subarray
this can be an alternative to traditional sliding window technique

this builds on the fact that the subarray at each pass would be either itself, or the localised maximum subarray

Optimised Time Complexity: O(n)
Optimised Space Complexity: O(1)
'''
# Question assumes that we are trying to find the maximum value in a given subarray
def kadane_maximum(arr):
    # assuming that the array has at least 1 element
    global_max, local_max = arr[0]
    for _, value in enumerate(arr):
        local_max = max(value, value + local_max)
        if (local_max > global_max):
            global_max = local_max
    return global_max
