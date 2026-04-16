# # Zadanie 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubed = [number ** 3 for number in numbers]

for item in cubed:
    if item % 2 != 0:
        print(item)


# # Zadanie 2

list_of_numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

non_zero_indexes = [idx for idx, x in enumerate(list_of_numbers) if x != 0]


zero_ranges = []
for i in range(len(non_zero_indexes) - 1):
    zero_ranges.extend(list_of_numbers[non_zero_indexes[i] + 1:non_zero_indexes[i + 1]])
zero_ranges.extend(list_of_numbers[non_zero_indexes[-1] + 1:])

print(zero_ranges)



non_zero_ranges = [list_of_numbers[idx] for idx in non_zero_indexes]

print(non_zero_ranges)
