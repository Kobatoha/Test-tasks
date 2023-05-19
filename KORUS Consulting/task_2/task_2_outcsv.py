import csv


def max_sequence_length(csv_file):
    # Открываем файл и построчно добавляем в список значения, игнорируя не-int значения
    numbers = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                    numbers.append(int(item))

    max_sequence = []
    current_sequence = []

    # Проходимся по списку чисел, находим положительные последовательности
    for num in numbers:
        if num > 0:
            current_sequence.append(int(num))
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = []

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence
        
    # Открываем файл для записи и записываем результат выполнения функции
    with open(csv_file[:-4] + '_out.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['max_length'])
        writer.writerow([len(max_sequence)])

