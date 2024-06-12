def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    # if value can't be found
    return -1 