# TODO импортировать необходимые молули
import  json
import  csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
      # TODO считать содержимое csv файла
      with open(INPUT_FILENAME, 'r') as file:

          reader = csv.DictReader(file)

          data = list(reader)

      # TODO Сериализовать в файл с отступами равными 4
      with open(OUTPUT_FILENAME, 'w') as output_file:
          json.dump(data, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Печать содержимого созданного JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
