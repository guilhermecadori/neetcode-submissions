from typing import List

def read_integers() -> List[int]:
    user_input = input()

    list_input = user_input.split(",")
    list_int = []
    for item in list_input:
        list_int.append(int(item))
    return list_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
