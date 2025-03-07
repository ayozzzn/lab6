from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

nums = [2, 3, 4, 5]
print("Product of list:", multiply_list(nums))
