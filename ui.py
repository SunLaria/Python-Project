from functions import startup, choose_user_task, choose_category_task, view_all_users_tasks,all_users_tasks, border, edit_task, delete_task, view_sorted_tasks, verify_uppercase, end_date_define, extend_task
from crud import create_task
import datetime
import os


def create_menu():
    """task creation menu"""
    errors = []
    border()
    print()
    taskname = input("Task Name: ")
    taskname = verify_uppercase(taskname)
    print()
    end_date = end_date_create(creation_date=datetime.date.today())
    print()
    responsible_person = choose_user_task()
    border()
    print()
    description = input("Task description: ")
    description = verify_uppercase(description)
    category = choose_category_task(responsible_person)
    task_info = [taskname,responsible_person,description,category]
    for info in task_info:
        if info == "" or info.isspace() == True:
            errors.append(info)
    if len(errors) > 0:
        border()
        print()
        return f'One or more Task info is wrong'
    else:
        try:
            border()
            return create_task(name=taskname,end_date=end_date,responsible_person=responsible_person,description=description,category=category)
        except:
            border()
            print()
            return "task creation went bad"

def view_menu():
    """view all tasks menu"""
    while True:
        border()
        print()
        all_tasks = all_users_tasks()
        view_all_users_tasks(tasks_list=all_tasks)
        print()
        choice = input("Choose Task Number Or [B]ack To Menu: ")
        choice = verify_uppercase(choice)
        if choice != "" and choice.isspace() == False and choice.isnumeric() == True and int(choice) != 0 and int(choice) <= len(all_tasks):
            task_menu(task=all_tasks[int(choice)-1])
        elif choice == "B":
            break

def view_sorted_menu(sort_word:str = "responsible_person"):
    """view all tasks menu in a sorted way"""
    while True:
        border()
        print()
        all_tasks = all_users_tasks()
        sort_keys = {"Name":"name","End Date":"end_date","Responsible Person":"responsible_person","Category":"category"}
        view_sorted_tasks(tasks_list=all_tasks,sort_word=sort_keys[sort_word])
        print()
        choice = input("Choose Task Number Or [B]ack: ")
        choice = verify_uppercase(choice)
        if choice != "" and choice.isspace() == False and choice.isnumeric() == True and int(choice) != 0 and int(choice) <= len(all_tasks):
            task_menu(task=all_tasks[int(choice)-1])
        elif choice == "B":
            break


def edit_menu(task:object = "task"):
    """edit menu"""
    while True:
        edit_keys = ["Name","End Date","Responsible Person","Description","Category"]
        choice = input("Please Enter The Category You Would Like To Edit Or [B]ack: ")
        choice = verify_uppercase(choice)
        if choice != "" and choice.isspace() == False:
            if choice == "B":
                break
            if choice in edit_keys:
                print()
                return edit_task(task=task,choice=choice)
                
def sort_menu():
    """view all tasks sort menu"""
    while True:
        border()
        print()
        sort_keys = ["Name","End Date","Responsible Person","Category"]
        print("Sort Word Options:\n\nName, End Date, Responsible Person, Category")
        print()
        choice = input("Please Enter The Sort Search Word Or [B]ack To Menu: ")
        choice = verify_uppercase(choice)
        if choice != "" and choice.isspace() == False:
            if choice == "B":
                break
            elif len(choice.split(" ")) == 2:
                choice = " ".join(map(lambda x: x.title(),choice.split(" ")))
        if choice in sort_keys:
            print()
            view_sorted_menu(sort_word=choice)


def task_menu(task:object="default_task"):
    """view task info with features"""
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
        choice = input("[E]dit, E[X]tand, [D]elete, [B]ack To Menu: ")
        choice = verify_uppercase(choice)
        if choice == "E":
            print(edit_menu(task))
        elif choice == "X":
            extend_task(task=task)

        elif choice == "D":
            choice = input("Delete Confirmation Y\\N: ")
            choice = verify_uppercase(choice)

            if choice == "Y":
                print(delete_task(task))
                break
            else:
                print('Task Delete Cancelled')
            

        elif choice == "B":
            break

def end_date_create(creation_date:tuple):
    """end date creation"""
    while True:
        border()
        print()
        date_keys = {"Y":"Years","D":"Days","M":"Months"}
        date_key = input("Task Period:\n\n[D]ays, [M]onthes, [Y]ears: ")
        date_key = verify_uppercase(date_key)

        if date_key != "" and date_key.isspace() == False:
            if date_key in date_keys.keys():
                print()
                number= input(f"How Many {date_keys[date_key]}: ")
                if number.isdigit() == True and int(number) > 0:
                    return end_date_define(creation_date=creation_date,num=number,choice=date_key)
            
def main_menu():
    """app main menu"""
    os.system('cls')
    startup()
    print()
    choice = input("""---------  Task manager ---------
1. Create Task
2. View Organization Tasks 
3. Show Sorted Tasks
4. Exit
    Your choice?: """)
    
    if choice == "1":
        print(create_menu())
        print()
        input("Press Any Key To Continue..")
    elif choice == "2":
        view_menu()
    elif choice == "3":
        print(sort_menu())
    elif choice =="4":
        quit()