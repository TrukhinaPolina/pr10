import json


def write_to_json(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_from_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data


def add_data():
    data = read_from_json()
    name = input("Введите название: ")
    price = input("Введите цену: ")
    data[name] = price
    write_to_json(data)


# Главная функция
def main():
    data = {}
    write_to_json(data)

    add_data()

    data = read_from_json()
    for name, price in data.items():
        print('Название:', f"{name}")
        print('Цена:', f"{price}")


if __name__ == "__main__":
    main()
