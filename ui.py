from functions import startup, create_user, view_users, delete_user, choose_user_task, choose_category_task, create_task
import datetime

def moderator_menu():
    while True:
        choice = input("""---------  Moderator Menu ---------
1. View All Users
2. Create New User
3. Delete User
4. Exit To Main Menu
                   
""")
        if choice == "2":
            print(create_user(input("Enter User Name To Register: ")))
        elif choice == "1":
            print(view_users())
        elif choice == "3":
            delete_user(input("User Name To Delete: "))
        elif choice == "4":
            break



def create_menu():
    errors = []
    taskname = input("Task Name: ")
    end_date = input("End Date: ")
    responsible_person = choose_user_task()
    description = input("Task description: ")
    category = choose_category_task(responsible_person)
    task_info = [taskname,end_date,responsible_person,description,category]
    for info in task_info:
        if info =="" or info.isspace()== True:
            errors.append(info)
    if errors > 0:
        return f'One or more Task info is wrong'
    else:
        try:
            create_task(name=taskname,end_date=end_date,responsible_person=responsible_person,description=description,category=category)
        except:
            return "task creation went bad"

def main_menu():
    startup()
    print()
    choice = input("""---------  Task manager ---------
1. Create Task
2. View All Organization Tasks 
3. Show Filtered Tasks
4. Moderator""")
    
    if choice == "1":
        print(create_menu())
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        moderator_menu()