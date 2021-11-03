import os
from pprint import pprint

with open('recept.txt', encoding='utf-8') as fale:
    cook_book = {}
    for dinner in fale:
        dish_name = dinner.strip()
        counter = int(fale.readline().strip())
        cook_box = []
        for ingr in range(counter):
            ingredient_name, quantity, measure = fale.readline().split('|')
            cook_box.append({'ingredient_name':ingredient_name.strip(), 'quantity':int(quantity.strip()), 'measure':measure.strip()})
        cook_book[dish_name] = cook_box
        fale.readline()

# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
def get_shop_list_by_dishes(dishes, person_count):
    rezult = {}
    options = {}
    person_count = float(person_count)
    for dish1 in dishes:
        if dish1 in cook_book.keys():
            for status in cook_book.get(dish1):
                options['measure'] = status.get('measure')
                options['quantity'] = int(status.get('quantity')) * person_count
                rezult[status['ingredient_name']] = options
    print(rezult)

get_shop_list_by_dishes(['Омлет','Фахитос'], 9)

