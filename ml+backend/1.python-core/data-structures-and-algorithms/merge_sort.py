def merge_sort(list):

    if len(list) <= 1:
        return list
    
    left, right = split(list)
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def split(list):

    mid = len(list)//2

    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1 

    return l

def verify(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    else:
        return list[0] < list[1] and verify(list[1:])

test_list = [3,1,4,2]

sorted_list = merge_sort(test_list)
print(sorted_list)

verified = verify(sorted_list)
print(verified)