import sqlite3
from tabulate import tabulate


def create_dummies(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO persons (first_name, last_name, gender, birth_date, death_date, place_of_birth) VALUES (?, ?, ?, ?, ?, ?);", ("init", "init", "init", "init","init","init"))
    conn.commit()
    cursor.execute("""UPDATE sqlite_sequence SET seq = 999 WHERE name = 'persons';""")
    conn.commit()

    cursor.execute("INSERT INTO relation_types (type_name) VALUES ('init');")
    conn.commit()
    cursor.execute("""UPDATE sqlite_sequence SET seq = 999 WHERE name = 'relation_types';""")
    conn.commit()

    cursor.execute("INSERT INTO relationships (from_id, to_id, type_id) VALUES (0, 0, 0);")
    conn.commit()
    cursor.execute("""UPDATE sqlite_sequence SET seq = 999 WHERE name = 'relationships';""")
    conn.commit()

    conn.close()


def verify_dummies(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM persons;")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="psql"))

    cursor.execute("SELECT * FROM relationships;")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="psql"))

    cursor.execute("SELECT * FROM relation_types;")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="psql"))

    conn.close()


def add_person(conn, cursor, first_name, last_name, gender, birth_date, death_date, place_of_birth):

    cursor.execute("INSERT INTO persons(first_name, last_name, gender, birth_date, death_date, place_of_birth) VALUES (?, ?, ?, ?, ?, ?);",(first_name, last_name, gender, birth_date, death_date, place_of_birth))
    conn.commit()

    cursor.execute("SELECT * FROM persons")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="psql"))


def add_relation_type(conn, cursor, type_name):
    cursor.execute("INSERT INTO relation_types(type_name) VALUES (?);", (type_name,))
    conn.commit()

    cursor.execute("SELECT * FROM relation_types;")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="psql"))


def add_relationship(conn, cursor, from_id, to_id, type_id):
    cursor.execute("INSERT INTO relationships(from_id, to_id, type_id) VALUES (?,?,?);", (from_id, to_id, type_id))
    conn.commit()

    cursor.execute("SELECT * FROM relation_types;")
    results = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    print(tabulate(results, headers=headers, tablefmt="psql"))