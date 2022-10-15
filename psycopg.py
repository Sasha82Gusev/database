import psycopg2

def start_db(): # Cоздаем структуру БД
    with conn.cursor() as cursor:
        cursor.execute("CREATE  TABLE IF NOT EXISTS client (id_client serial PRIMARY KEY, client_name varchar(40) not null, client_famil varchar(40) not null, client_email varchar(40));")
        cursor.execute("CREATE  TABLE IF NOT EXISTS phone (id_phone serial PRIMARY KEY,	id_client serial REFERENCES client(id_client), phone_number varchar(40) not null);")


def create_db():   #Заполняем базу данных из SQL файла db_creaate.sql
    with open("db_create.sql", "r") as file1:
        lines = file1.readlines()
        with conn.cursor() as cursor:
            for line in lines:
                #print(line)
                cursor.execute(line)


def add_client(name, soname, mail):
    if mail == ",''":
        mail = ""
    # print(mail)
    strin = "INSERT INTO client VALUES (DEFAULT" + soname + name + mail + ");"
    # print(strin)
    with conn.cursor() as cursor:
        cursor.execute(strin)


def add_phone(phone, id):
    strin = "INSERT INTO phone VALUES (DEFAULT" + id + phone + ");"
    # print(strin)
    with conn.cursor() as cursor:
        cursor.execute(strin)


def change_client(id, name, soname, mail):
    if mail == "''":
        mail = "NULL"
    # print(mail)
    # UPDATE client SET client_famil = 'Guskin', client_name ='Shura' WHERE id_client = 5
    strin_name = "UPDATE client SET client_name = " + name + " WHERE id_client = " + str(id)
    strin_soname = "UPDATE client SET client_famil = " + soname + " WHERE id_client = " + str(id)
    strin_mail = "UPDATE client SET client_email = " + mail + " WHERE id_client = " + str(id)
    # print(strin_name)
    # print(strin_soname)
    # print(strin_mail)
    with conn.cursor() as cursor:
        cursor.execute(strin_name)
        cursor.execute(strin_soname)
        cursor.execute(strin_mail)


def del_phone(phone, id):
    # DELETE FROM phone WHERE phone_number ='243' AND id_client = 5
    strin = "DELETE FROM phone WHERE phone_number =" + phone + " AND id_client = " + str(id) + ";"
    # print(strin)
    with conn.cursor() as cursor:
        cursor.execute(strin)


def del_client(id):
    # DELETE FROM phone WHERE phone_number ='243' AND id_client = 5
    strin = "DELETE FROM phone WHERE id_client = " + str(id) + "; DELETE FROM client WHERE id_client = " + str(id) + ";"
    # print(strin)
    with conn.cursor() as cursor:
        cursor.execute(strin)


def find(findstring):
    # SELECT DISTINCT c.id_client FROM client AS c LEFT JOIN phone  AS ph ON c.id_client = ph.id_client WHERE client_name LIKE '%ru%' OR client_famil LIKE '%ru%' OR client_email LIKE '%ru%';
    strin = "SELECT DISTINCT c.id_client, client_name \
        FROM client AS c LEFT JOIN phone  AS ph ON c.id_client = ph.id_client \
        WHERE client_name LIKE '%" + findstring + "%' OR client_famil LIKE '%" + findstring + "%' OR client_email LIKE '%"\
        + findstring + "%' OR phone_number LIKE '%" + findstring + "%';"
    print(strin)
    with conn.cursor() as cursor:
        cursor.execute(strin)
        prstr = cursor.fetchall()
        print(prstr)


if __name__ == "__main__":
    with psycopg2.connect(dbname='client_db', user='postgres', password='41321122', host='localhost') as conn:
        start_db()
        print('Что вы хотите сделать?')
        print('0. Очистить БД и заполнить её значениями для примера')
        print('1. Добавить нового клиента')
        print('2. Добавить телефон для существующего клиента')
        print('3. Изменить данные о клиенте')
        print('4. Удалить телефон для существующего клиента')
        print('5. Удалить существующего клиента(вместе с телефонами)')
        print('6. Найти клиента по его данным')
        action = int(input(''))
        if action == 0:
            create_db()
        if action == 1:
            name = ",'" + input('Введите Имя ') + "'"
            soname = ",'" + input('Введите Фамилию ') + "'"
            mail = ",'" + input('Введите электронку ') + "'"
            add_client(name, soname, mail)
        if action == 2:
            phone = ",'" + input('Введите телефон ') + "'"
            id = ",'" + input('ID Клиента ') + "'"
            add_phone(phone, id)
        if action == 3:
            id = int(input('ID Клиента '))
            name = "'" + input('Введите Имя (Enter-не менять) ') + "'"
            if name == "''":
                name = "client_name"
            soname = "'" + input('Введите Фамилию (Enter-не менять) ') + "'"
            if soname == "''":
                soname = "client_famil"
            mail = "'" + input('Введите электронку (Enter-не менять) ') + "'"
            if mail == "''":
                mail = "client_email"
            change_client(id, name, soname, mail)
        if action == 4:
            phone = "'" + input('Введите телефон ') + "'"
            id = input('ID Клиента ')
            del_phone(phone, id)
        if action == 5:
            id = input('ID Клиента ')
            del_client(id)
        if action == 6:
            findstring = input('Что ищем? ')
            find(findstring)
