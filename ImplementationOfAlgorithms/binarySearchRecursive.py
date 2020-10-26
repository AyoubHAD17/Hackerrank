def binarySearchRecursive(array, x, left, right):
    if left > right:
        return False

    mid = (left + right) // 2

    if array[mid] == x:
        return True
    elif x < array[mid]:
        return binarySearchRecursive(array, x, left, mid - 1)
    else:
        return binarySearchRecursive(array, x, mid + 1, right)

def binarySearchIterative(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == x:
            return True
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
    
