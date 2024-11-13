# TODO решите задачу
import json


FILE = "input.json"


def task() -> float:
    with open(FILE) as f:
        data_ = json.load(f)

        score_and_weight = [item["score"] * item["weight"] for item in data_]
        return round(sum(score_and_weight), 3)


if __name__ == '__main__':
    print(task())
