import json
with open('q.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
for product in data['products']:
    print('Название:', product['name'])
    print('Цена:', product['price'], "руб.")
    print('Вес:', product['weight'], "гр.")
    if product['available']:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print()
