# def add_two_numbers() -> int:
#     args_chars = input()
#     args_nums = args_chars.split(",")
#     arg_list = []
#     for arg in args_nums:
#         arg_list.append(int(arg))
#     return sum(arg_list)

def add_two_numbers() -> int:
    a, b = input().split(",")
    return int(a) + int(b)

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
