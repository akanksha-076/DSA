# gien an array [33,34,35,36,373,38,39]
# we have to sort it using queue the odd number comes at frist and the even comes at end
from collections import deque

def sort_odd_even_queue(arr):
    odd_queue = deque()
    even_queue = deque()

    # Dequeue each element and separate into odd/even
    for num in arr:
        if num % 2 != 0:
            odd_queue.append(num)
        else:
            even_queue.append(num)

    # Merge: odds first, then evens
    result = []
    while odd_queue:
        result.append(odd_queue.popleft())
    while even_queue:
        result.append(even_queue.popleft())

    return result


arr = [33, 34, 35, 36, 373, 38, 39]
print("Original:", arr)
print("Sorted:  ", sort_odd_even_queue(arr))