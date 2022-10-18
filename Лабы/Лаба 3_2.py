list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_number = list_numbers[0]
max_index = 0
for a, b in enumerate(list_numbers):
    if b > max_number:
        max_number = b
        max_index = a
list_numbers[max_index] = list_numbers[-1]
list_numbers[-1] = max_number


print(list_numbers)
