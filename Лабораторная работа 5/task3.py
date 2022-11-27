import random
def get_unique_list_numbers(list_) -> list[int]:
    while len(list_) < 15:
        i = random.randint(-10, 10)
        if i not in list_:
            list_.append(i)
    return list_
list_unique_numbers = []
list_unique_numbers = get_unique_list_numbers(list_unique_numbers)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
