from functions import startup, create_user, view_users, delete_user, choose_user_task, choose_category_task, create_task
import datetime


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
    if len(errors) != 0:
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
    Your choice?: """)
    
    if choice == "1":
        print(create_menu())
    elif choice == "2":
        pass
    elif choice == "3":
        pass