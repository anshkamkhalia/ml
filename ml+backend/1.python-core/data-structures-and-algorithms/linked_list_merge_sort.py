from linked_list import LinkedList

def merge_sort(linked_list):

    if linked_list.is_empty() or linked_list.size_of_list() == 1:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)

    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):

    if linked_list.is_empty() or linked_list.head.next_node is None:

        left = linked_list
        right = LinkedList()  
        return left, right

    mid = linked_list.size_of_list() // 2
    mid_node = linked_list.search_at_index(mid - 1)

    left = linked_list
    right = LinkedList()
    right.head = mid_node.next_node
    mid_node.next_node = None 

    return left, right

def merge(left, right):

    merged = LinkedList()
    merged.add(0)  
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head and right_head:

        if left_head.data < right_head.data:
            current.next_node = left_head
            left_head = left_head.next_node

        else:

            current.next_node = right_head
            right_head = right_head.next_node
        current = current.next_node

    if left_head:

        current.next_node = left_head
    elif right_head:
        
        current.next_node = right_head

    merged.head = merged.head.next_node

    return merged
