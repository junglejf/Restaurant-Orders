import csv


def open_log(path_to_file):
    with open(path_to_file, 'r') as file:
        dict_orders = {}
        name, food, week_day = 0, 1, 2  # [name, food, week_day] in file
        food_list, open_days = set(), set()
        orders = csv.reader(file)
        for order in orders:
            food_list.add(order[food])
            open_days.add(order[week_day])

            if order[name] not in dict_orders:
                dict_orders[order[name]] = {}
                dict_orders[order[name]] = {
                    "week_day": set([order[week_day]]),
                    'food': {order[food]: 1}
                    }
            else:
                dict_orders[order[name]]["week_day"].add(order[week_day])

                if order[food] not in dict_orders[order[name]]['food']:
                    dict_orders[order[name]]['food'][order[food]] = 1
                else:
                    dict_orders[order[name]]['food'][order[food]] += 1

    return dict_orders, food_list, open_days


def save_log(dict_orders, food_list, open_days):
    maria_favorite_food = max(
        dict_orders['maria']['food'],
        key=dict_orders['maria']['food'].get)
    print('\nQual o prato mais pedido por maria?', maria_favorite_food)
    print(
        'Quantas vezes arnaldo pediu hamburguer?',
        dict_orders['arnaldo']['food']['hamburguer'])

    joao_foods = set((dict_orders['joao']['food']).keys())
    joao_week_day = dict_orders['joao']['week_day']
    print('Quais pratos joao nunca pediu?', food_list - joao_foods)
    print('Quais dias joao nunca foi à lanchonete?', open_days - joao_week_day)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(maria_favorite_food + '\n')
        hamburguers = str(dict_orders['arnaldo']['food']['hamburguer']) + '\n'
        file.writelines(hamburguers)
        file.write(str(food_list - joao_foods) + '\n')
        file.write(str(open_days - joao_week_day) + '\n')


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida: {str(path_to_file)}')

    try:
        dict_orders, food_list, open_days = open_log(path_to_file)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{str(path_to_file)}'")

    else:
        save_log(dict_orders, food_list, open_days)
