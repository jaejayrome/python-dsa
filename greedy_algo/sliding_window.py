import math

'''
Brute Force Solution
finding the subarray starting at every single pass
recomputing the other k - 1 elements
'''

'''
Fixed Sliding Window Technique
At each pass, subtract the element that leaves the window
then add the element that enters the window

Time Complexity: O(n)
'''
def fixed_sliding_window(arr, k):
    total = sum(arr[:k])
    maxTotal = total
    for i in range(len(arr) - k):
        total -= arr[i]
        total += arr[i+k]
        maxTotal = max(maxTotal, total)
    return maxTotal

'''
Brute Force Solution
Example Problem: finding the smallest subarray such that the sum of elements
is greater than or equals to a value S

Time Complexity: O(n^2)
'''
def brute_force_dynamic(arr, s):
    minimumSize = math.inf
    for i  in range(len(arr) - 1):
        currTotal = arr[i]
        currSize = 1
        for j in range(i, len(arr) - 1):
            currTotal += arr[j]
            currSize += 1
            if currTotal >= s:
                break
        minimumSize = min(currSize, minimumSize)
    return minimumSize


'''
Dynamic Sliding Window Technique
We don't know how big the size of the window

this would leverage on the use of 2 pointers
at every pass, keep moving the right pointer to the right (increase the window)
then based on the condition, we would move the left pointer to the right (shrink the window)
'''
def dynamic_sliding_window(arr, s):
    minSize = math.inf
    sum = 0
    l = 0
    # open the window
    for r in range(len(arr) - 1):
        sum += arr[r]
        while (sum >= s):
            # see whether this "window" is the smallest
            minSize = min(minSize, r - l + 1)
            # close the window
            sum -= arr[l]
            l += 1