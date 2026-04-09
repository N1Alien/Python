# # Zadanie 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubed = [number ** 3 for number in numbers if number % 2 != 0]

print(cubed)

# # Zadanie 2

list_of_numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
zero_ranges = list_of_numbers.copy()

non_zero_indexes = [idx for idx, x in enumerate(list_of_numbers) if x != 0]

# # # # # # # # # # # # # # # # # # # # # # # 

zero_ranges = []
for i in range(len(non_zero_indexes)):
    start = non_zero_indexes[i] +1

    if len(non_zero_indexes) == i + 1:
        end = len(list_of_numbers)
    else:
        end = non_zero_indexes[i +1]

    if start < end:
        zero_ranges.extend(list_of_numbers[start:end])



print(zero_ranges)

# # # # # # # # # # # # # # # # # # # # # # # 

non_zero_ranges = []
for i in range(len(non_zero_indexes)):
    start = non_zero_indexes[i]
    end = non_zero_indexes[i] +1
    if start < end:
        non_zero_ranges.extend(list_of_numbers[start:end])



print(non_zero_ranges)