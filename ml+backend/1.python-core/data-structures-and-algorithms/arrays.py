newList = [1, 2, 3]
result = newList[0]

try:
    result = newList[4]
    print(result)
except Exception as e:
    print(e)

numbers = []
numbers.append(1)
print(len(numbers))

numbers.append(10)
print(len(numbers))

numbers = []
numbers.extend([1,2,3])
print(numbers)

numbers.remove(1)
print(numbers)

