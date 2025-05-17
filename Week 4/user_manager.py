from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

#update Funtion of advanced search
def advanced_search_user(user_id, name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? AND name LIKE ?", (user_id, '%' + name + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_course(course_id, name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (id, name, unit) VALUES (?, ?, ?)", (course_id, name, unit))
        conn.commit()
        print(" Course added.")
    except sqlite3.IntegrityError:
        print(" Course ID must be unique.")
    conn.close()

def search_course_with_user(course_id, user_name):
    conn = create_connection()
    cursor = conn.cursor()
    # You are combining data from users and courses here; assuming no relationship yet, just independent search
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + user_name + '%',))
    users = cursor.fetchall()
    
    cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
    course = cursor.fetchone()
    
    conn.close()
    return users, course
# This function is for searching courses with a specific user name

def assign_course_to_user(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO user_courses (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
        conn.commit()
        print("Course assigned to user.")  # Fixed indentation
    except sqlite3.IntegrityError:
        print("Assignment already exists or invalid IDs.")
    conn.close()

def get_courses_for_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT c.id, c.name, c.unit
            FROM courses c
            JOIN user_courses uc ON c.id = uc.course_id
            WHERE uc.user_id = ?
        ''', (user_id,))
        courses = cursor.fetchall()
        if not courses:
            print(f"No courses found for user ID {user_id}.")
        return courses
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()
# This function is for getting courses for a specific user
