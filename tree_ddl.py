import sqlite3

def connect_db(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    return conn, cursor


def create_persona(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            person_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT,
            gender TEXT,
            birth_date DATE,
            death_date DATE,
            place_of_birth TEXT
            );
        """)


def create_relationships(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relationships (
            rel_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_id INTEGER NOT NULL,
            to_id INTEGER NOT NULL,
            type_id INTEGER NOT NULL,
            FOREIGN KEY (from_id) REFERENCES persons(person_id),
            FOREIGN KEY (to_id) REFERENCES persons(person_id),
            FOREIGN KEY (type_id) REFERENCES relation_types(type_id)
            );
        """)


def create_rel_types(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relation_types (
            type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT UNIQUE NOT NULL
            );
        """)


def create_db(path):
    conn, cursor = connect_db(path)
    create_persona(cursor)
    create_relationships(cursor)
    create_rel_types(cursor)
    conn.commit()
    conn.close()