import random
import time

nums = [random.randint(1,10000) for x in range(1,11)]

def is_sorted(list):
    for index in range(len(list)-1):
        if list[index] <= list[index+1]:
            continue
        else:
            return False
    return True

def bogo_sort(values):
    counter = 0
    while not is_sorted(values):
        random.shuffle(values)
        counter += 1
    print(counter)
    return values

start_time = time.time()
sorted_list = bogo_sort(values=nums)
end_time = time.time()

print("Sorted list:", sorted_list)
print(f"Time taken: {end_time - start_time:.4f} seconds")
