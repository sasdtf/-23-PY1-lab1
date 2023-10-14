list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
total_players = len(list_players)

team1 = list_players[:total_players // 2]
team2 = list_players[total_players // 2:]

print(team1)
print(team2)

