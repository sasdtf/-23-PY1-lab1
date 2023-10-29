# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    first_words = first_group.split(separator)
    second_words=second_group.split(separator)

    first_set = set(first_words)
    second_set = set(second_words)

    common_participants = first_set & second_set

    # Сортируем полученное множество общих участников
    common_participants = sorted(list(common_participants))

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(first_group=participants_first_group,second_group= participants_second_group , separator="|")
print("Общие участники:", result)
# TODO Провеьте работу функции с разделителем отличным от запятой
