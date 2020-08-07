def binary_search(arr, target, start, end):
    if start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            return binary_search(arr, target, start, middle-1)
        else:
            return binary_search(arr, target, middle+1, end)
    else:
        return -1

# RECURSIVE IMPLEMENTATION:
def recursive_agnostic_binary_search(arr, target, start, end):
    if start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[start] < arr[end]:
            if target < arr[middle]:
                return recursive_agnostic_binary_search(arr, target, start, middle-1)
            else:
                return recursive_agnostic_binary_search(arr, target, middle+1, end)
        else:
            if arr[middle] < target:
                return recursive_agnostic_binary_search(arr, target, start, middle-1)
            else:
                return recursive_agnostic_binary_search(arr, target, middle+1, end)
    else:
        return -1

# ITERATIVE IMPLEMENTATION:
def iterative_agnostic_binary_search(arr, target):
    if 0 < len(arr):
        start = 0
        end = len(arr) - 1
        while start <= end:
            middle = (start + end) // 2
            if arr[middle] == target:
                return middle
            elif arr[start] < arr[end]:
                if target < arr[middle]:
                    end = middle-1
                elif arr[middle] < target:
                    start = middle+1
            else:
                if arr[middle] < target:
                    end = middle-1
                elif target < arr[middle]:
                    start = middle+1
    return -1
