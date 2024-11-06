# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, separator = ","):

    new_participants_first = set(participants_first.split(separator))
    new_participants_second = set(participants_second.split(separator))
    group = list(new_participants_first.intersection(new_participants_second))
    group.sort()
    return (group)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(participants_first_group, participants_second_group, ".")
