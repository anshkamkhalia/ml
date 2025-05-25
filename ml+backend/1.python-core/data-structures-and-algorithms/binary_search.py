def binary_search(target, inputs):
    first = 0
    last = len(inputs)-1
    inputs.sort()

    while first <= last:
        midpoint = last-first//2

        if inputs[midpoint] == target:
            return midpoint
        
        elif inputs[midpoint] < target:
            first = midpoint+1

        else:
            last = midpoint-1
    
    return None

def verify(position):
    
    if position is not None:
        print(f"Target found at position {position}")
    else:
        print("Target not found")

target = 100
inputs = [num for num in range(101)]

verify(position=binary_search(target=target, inputs=inputs))