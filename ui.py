from functions import startup, choose_user_task, choose_category_task, create_task, view_all_users_tasks,all_users_tasks, border
import datetime
import os


def create_menu():
    errors = []
    border()
    taskname = input("Task Name: ")
    border()
    end_date = input("End Date: ")
    responsible_person = choose_user_task()
    border()
    description = input("Task description: ")
    category = choose_category_task(responsible_person)
    task_info = [taskname,end_date,responsible_person,description,category]
    for info in task_info:
        if info == "" or info.isspace() == True:
            errors.append(info)
    if len(errors) > 0:
        return f'One or more Task info is wrong'
    else:
        try:
            border()
            return create_task(name=taskname,end_date=end_date,responsible_person=responsible_person,description=description,category=category)
        except:
            return "task creation went bad"

def view_menu():
    all_tasks = all_users_tasks()
    while True:
        view_all_users_tasks()
        print()
        choice = input("Choose Task Number Or [M]ain menu: ".title())
        if choice != "" and choice.isspace() == False and choice.isnumeric() == True and int(choice) != 0 and int(choice) <= len(all_tasks):
            task_menu(task=all_tasks[int(choice)-1])
        elif choice == "M":
            break
        
def task_menu(task:object="default_task"):
    while True:
        border()
        print()
        print(f"""task info:
        Name: {task.name}
        Creation Date: {task.creation_date}
        End Date: {task.end_date}
        Responsible Person: {task.responsible_person}
        Description : {task.description}
        Category: {task.category}""".title())
        print()
        choice = input("[E]dit, E[X]pand, [D]elete, [B]ack to menu: ")
        if choice == "E":
            pass
        elif choice == "X":
            pass
        elif choice == "D":
            pass
        elif choice == "B":
            break

def main_menu():
    os.system('cls')
    startup()
    print()
    choice = input("""---------  Task manager ---------
1. Create Task
2. View Organization Tasks 
3. Show Filtered Tasks
4. Exit
    Your choice?: """)
    
    if choice == "1":
        print(create_menu())
        print()
        input("Press Any Key To Continue..")
    elif choice == "2":
        view_menu()
    elif choice == "3":
        pass
    elif choice =="4":
        quit()