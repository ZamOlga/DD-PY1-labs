# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator = ','):
    first_group = set(first_group.split(separator))
    second_group = second_group.split(separator)
    common_part = list(first_group.intersection(second_group))
    common_part.sort()
    return common_part

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(f'{find_common_participants(participants_first_group,participants_second_group,separator = "|")}')
# TODO Провеьте работу функции с разделителем отличным от запятой
