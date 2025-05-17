import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def create_course_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_user_courses_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_courses (
            user_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY (user_id, course_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    ''')
    conn.commit()
    conn.close()

