# TODO решите задачу
import json
def task() -> float:
    with open("input.json") as file:
        data = json.load(file)
    # print("Десериализованные данные из JSON файла в python объект:", data)
    result = 0
    for item in data:
        result += item["score"] * item["weight"]
    return round(result, 3)

print(task())
