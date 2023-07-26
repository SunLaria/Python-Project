from functions import startup, choose_user_task, choose_category_task, view_all_users_tasks,all_users_tasks, border, edit_task, delete_task
from crud import create_task
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
    while True:
        all_tasks = all_users_tasks()
        view_all_users_tasks(tasks_list=all_tasks)
        print()
        choice = input("Choose Task Number Or [M]ain menu: ".title())
        if choice != "" and choice.isspace() == False and choice.isnumeric() == True and int(choice) != 0 and int(choice) <= len(all_tasks):
            task_menu(task=all_tasks[int(choice)-1])
        elif choice == "M":
            break

def edit_menu(task):
    while True:
        edit_keys = ["Name","End Date","Responsible Person","Description","Category"]
        choice = input("Please Enter The Category You would like to edit or [B]ack: ".title())
        if choice != "" and choice.isspace() == False:
            if choice == "B":
                break
            if choice in edit_keys:
                print()
                return edit_task(task=task,choice=choice)
                
                
        


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
            print(edit_menu(task))
        elif choice == "X":
            pass
        elif choice == "D":
            choice = input("Delete Confirmation y\\n: ")
            if choice == "y":
                print(delete_task(task))
                break
            else:
                print('Task Delete Cancelled')
            
                

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