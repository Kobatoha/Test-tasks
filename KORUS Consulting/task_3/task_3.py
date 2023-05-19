import csv


def income(departments, operations):
    # Чтение данных из файлов формата csv
    with open(departments, encoding='utf-8') as f:
        reader = csv.reader(f)
        departments = [tuple(row) for row in reader][1:]  # пропускаем заголовок

    with open(operations, encoding='utf-8') as f:
        reader = csv.reader(f)
        operations = [tuple(row) for row in reader][1:]

    # Создание словаря с суммарной прибылью по месяцам
    profits = {}
    for op in operations:
        year, month, day, dep_id, income = op[1:]
        year, month, dep_id, income = int(year), int(month), int(dep_id), int(income)
        if any(year < int(dep[1]) or year > int(dep[2]) for dep in departments if int(dep[0]) == dep_id):
            continue  # пропускаем некорректные данные
        key = (year, month, next(dep[3] for dep in departments if int(dep[0]) == dep_id))
        profits[key] = profits.get(key, 0) + income

    # Преобразование словаря в список кортежей
    result = [(key[0], key[1], key[2], profits[key]) for key in sorted(profits)]

    # Возвращаем список кортежей
    return result

