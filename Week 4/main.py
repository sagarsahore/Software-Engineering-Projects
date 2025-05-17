from database import create_course_table, create_table, create_user_courses_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_search_user, add_course, search_course_with_user, assign_course_to_user, get_courses_for_user

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("=======================")
    print("6. Advanced Search (ID & Name)")
    print("=======================")
    print("7. Add Course")
    print("8. Search Course by Course ID & User Name")
    print("=======================")


def main():
    create_table()
    create_table()
    create_course_table()
    create_user_courses_table()
    print("Welcome to the User Manager!")
    while True:
        menu()
        choice = input("Select an option (1-8):")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            try:
                user_id = int(input("Enter user ID: "))
                name = input("Enter name: ")
                users = advanced_search_user(user_id, name)
                for user in users:
                    print(user)
                if not users:
                    print("No matching user found.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
                
        elif choice == '7':
            try:
                course_id = int(input("Enter course ID: "))
                name = input("Enter course name: ")
                unit = int(input("Enter course unit: "))
                add_course(course_id, name, unit)
            except ValueError:
                print("Invalid input. ID and unit must be numbers.")
        elif choice == '8':
            try:
                course_id = int(input("Enter course ID: "))
                user_name = input("Enter user name: ")
                users = search_course_with_user(course_id, user_name)
                for user in users:
                    print(user)
                if not users:
                    print("No matching course found.")
            except ValueError:
                print("Invalid input.") 
        elif choice == '9':
            try:
                user_id = int(input("Enter user ID: "))
                course_id = int(input("Enter course ID: "))
                assign_course_to_user(user_id, course_id)
            except ValueError:
                print("Invalid input. User ID and Course ID must be numbers.")
                
        elif choice == '10':
            try:
                user_id = int(input("Enter user ID: "))
                courses = get_courses_for_user(user_id)
                for course in courses:
                    print(course)
                if not courses:
                    print("No courses found for this user.")
            except ValueError:
                print("Invalid input. User ID must be a number.")
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
add_course(101, "Muay Thai Basics", 3)
add_course(102, "Explosive Speed Training", 2)
add_course(103, "Power & Conditioning", 4)
add_course(104, "Mental Toughness", 2)
add_course(105, "Advanced Striking", 3)