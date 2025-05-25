def recursiveBinarySearch(target, inputs):

    if len(inputs) == 0:
        return False

    else:
        midpoint = len(inputs) // 2
        if inputs[midpoint] == target:
            return True
        
        else:
            if inputs[midpoint] < target:
                
                return recursiveBinarySearch(target=target, inputs=inputs[midpoint+1:])
            else:
                return recursiveBinarySearch(target=target, inputs=inputs[:midpoint])

def verify(result):
    print(f"Target found: {result}")


target = 100
inputs = [num for num in range(101)]

verify(result=recursiveBinarySearch(target=target, inputs=inputs))