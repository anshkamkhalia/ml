def linearSearch(target, inputs):
    
    for index in range(0, len(inputs)):
        if inputs[index] == target:
            return index
    return None

def verify(index):
    if index is not None:
        print(f"Target found at position {index}")
    else:
        print("target not found")

inputs =[1,2,3,4,5,6,7]
target = 4

verify(index=linearSearch(target, inputs))