import psycopg2
import csv

readers = []

with open('readers.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    next(reader) # пропускаем заголовок
    for row in reader:
        person = {
            'id_library_ticket': row[0],
            'surname': row[1],
            'firstname': row[2],
            'lastname': row[3],
            'birthday': row[4],
            'gender': row[5],
            'adress': row[6],
            'phone_number': row[7]
        }
        readers.append(person)


# подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    port='5433',
    database="database",
    user="postgres",
    password="password"
)

# создание курсора
cur = conn.cursor()

# добавление данных из списка books в базу данных
for person in readers:
    cur.execute(
        "INSERT INTO readers (id_library_ticket, surname, firstname, lastname, birthday, gender, adress, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (book['id_library_ticket'], book['surname'], book['firstname'], book['lastname'], book['birthday'], book['gender'], book['adress'], book['phone_number'])
    )

# сохранение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()
