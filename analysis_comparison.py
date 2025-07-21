import time
import random
from heapsort import heapsort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(lesser) + equal + quicksort(greater)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return result + left + right

def test_sorting_algorithms():
    sizes = [100, 1000, 5000]
    for size in sizes:
        data = random.sample(range(size * 2), size)
        for alg in ['heapsort', 'quicksort', 'mergesort']:
            arr = data.copy()
            start = time.time()
            if alg == 'heapsort':
                heapsort(arr)
            elif alg == 'quicksort':
                quicksort(arr)
            elif alg == 'mergesort':
                mergesort(arr)
            end = time.time()
            print(f"{alg.capitalize()} on size {size}: {end - start:.6f} seconds")

if __name__ == "__main__":
    test_sorting_algorithms()
