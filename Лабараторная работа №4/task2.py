# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        dict_ = [line for line in csv.DictReader(f)] # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w') as out:
        json.dump(dict_, out, indent=4)# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
