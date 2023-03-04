with open('text.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        cook_book_name = line.strip()
        dishes_count = int(f.readline())
        dishes = []
        for i in range(dishes_count):
            emp = f.readline().strip()
            name, amount, measure = emp.split(' | ')
            dishes.append({
                'ingredient_name': name,
                'quantity': amount,
                'measure': measure
            })
        f.readline()
        cook_book[cook_book_name] = dishes
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            print(dish)
            for ingridient in cook_book[dish]:
                dict_dishes[ingridient['ingredient_name']] = {'quantity': ingridient['quantity'] * person_count, 'measure': ingridient['measure']}

    return dict_dishes


res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(res)