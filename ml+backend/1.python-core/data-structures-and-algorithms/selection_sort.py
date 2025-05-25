import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

unsorted = [8, 3, 6, 2, 1, 5]

start_time = time.time()
sorted_list = selection_sort(unsorted.copy()) 
end_time = time.time()

print("Sorted list:", sorted_list)
print(f"Time taken: {end_time - start_time:.4f} seconds")
