numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_of_numbers = 0
count_of_numbers = len(numbers)


for i in range(count_of_numbers):
    if numbers[i] == None:
        none_type_index = i
        continue
    sum_of_numbers += numbers[i]

average_of_numbers = sum_of_numbers/count_of_numbers
numbers[none_type_index] = average_of_numbers
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
