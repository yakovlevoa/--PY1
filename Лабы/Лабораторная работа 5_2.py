from random import randint


def get_unique_list_numbers() -> list[int]:
    random_numbers = []
    unique = []
    for _ in range(15):
        n = randint(-10, 10)
        while n in unique:
            n = randint(-10, 10)
        random_numbers.append(n)
        unique.append(n)
    return random_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
