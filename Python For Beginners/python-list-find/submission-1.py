from typing import List # this is used to add type hints for List type

# def find_index(nums: List[int], target: int) -> int:
#     return nums.index(target)


def find_index(nums: List[int], target: int) -> int:
    counter = -1
    for num in nums:
        counter += 1
        if num == target:
            return counter 

# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

