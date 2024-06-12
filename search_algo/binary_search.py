'''
Binary Search Algorithm 

takes the centre index at every pass
this assumes that the given array is sorted

Optimised Time Complexity: O(logN)
'''
# assuming that array has at least 1 element and that array is sorted
# target is the value that you are trying to find
def binarySearch(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high: 
        mid = (low + high) // 2
        midVal = arr[mid]
        if midVal < target:
            low = mid + 1
        elif midVal > target:
            high = mid - 1
        else:
            return mid
    # if value can't be found
    return -1
