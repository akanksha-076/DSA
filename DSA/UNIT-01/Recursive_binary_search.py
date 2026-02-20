def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)
        else:
            return binary_search(arr, mid+1, high, key)
    return -1

arr = [2, 4, 6, 8, 10, 12]
print(binary_search(arr, 0, len(arr)-1, 10))