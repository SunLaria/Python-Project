from crud import save,load
from myclass import Task
import datetime


def startup():
    """Starting up the app, verifying there is an saved pickle file, if not creating one"""
    try:
        load()
        print("Database found")
    except:
        save(data={})
        print("Database Created")
    return True

def create_user(user_name:str = "defualt_username"):
    """creates a user"""
    data = load()
    if user_name not in data.keys():
        data[user_name]={}
        data[user_name]={"tasks":[],"category":[]}
        save(data=data)
        return f"{user_name} user Created Successfully!"
    else:
        return f"{user_name} User Already Exists"

def view_users():
    data = load()
    border()
    if len(data.keys()) > 0:
        return f"All Users:\n\n{', '.join(data.keys())}"
    else:
        return f"All Users:\n\nNo Users Found in Database"

def delete_user(user_name:str="default_username"):
    choice = input("Delete Confirmation y\\n: ")
    if choice == "y":
        data = load()
        if user_name in data.keys():
            del data[user_name]
            save(data=data)
            print()
            return f"{user_name} Deleted Successfully"
        else:
            print()
            return f"{user_name} Not Found"
    else:
        return f"{user_name} Delete Cancelled"

def choose_user_task():
    while True:
        print(view_users())
        print()
        choice = input("Enter the responsible User for this task or [A]dd, [R]emove: ")
        print()
        if choice == "A":
            add_user = input("User Name to add: ")
            if add_user != "" and add_user.isspace() != True and add_user.isalpha() == True:
                print(create_user(add_user))
            else:
                print("Eror - User can only contain letters")

        elif choice == "R":
            del_user = input("User Name to Delete: ")
            if del_user != "" and del_user.isspace() != True and del_user.isalpha() == True:
                print()
                print(delete_user(del_user))
            else:
                print("Eror - User can only contain letters")
        else:
            data = load()
            for user in data.keys():
                if user == choice:
                    return user
            





def create_category(user_name:str = "defualt_username", category:str="default_category"):
    """creates a user"""
    data = load()
    data[user_name]["category"].append(category)
    save(data=data)
    return f"{category} Category Created Successfully!"


def view_categories(username):
    data = load()
    border()
    if len(data[username]["category"]) != 0:
        return f"All {username} Categories:\n\n{', '.join(data[username]['category'])}"
    else:
        return f"All {username} Categories:\n\nNo Categories For this User"


def delete_category(user_name:str="default_username",category:str = "defualt_category"):
    choice = input("Delete Confirmation: y\\n: ")
    if choice == "y":
        data = load()
        if category in data[user_name]["category"]:
            data[user_name]["category"].remove(category)
            save(data=data)
            print()
            return f"{category} Deleted Successfully"
        else:
            print()
            return f"{category} Not Found"
    else:
        return f"{category} Delete Cancelled"

def choose_category_task(username):
    while True:
        print(view_categories(username=username))
        print()
        choice = input("Enter the chosen category for this task or [A]dd, [R]emove: ")
        print()
        if choice == "A":
            add_categroy = input("Category Name to add: ")
            if add_categroy != "" and add_categroy.isspace() != True and add_categroy.isalpha() == True:
                print(create_category(user_name=username,category=add_categroy))
            else:
                print("Eror - Category can only contain letters")

        elif choice == "R":
            del_categroy = input("Category Name to Delete: ")
            if del_categroy != "" and del_categroy.isspace() != True and del_categroy.isalpha() == True:
                print()
                print(delete_category(user_name=username,category=del_categroy))
            else:
                print("Eror - Category can only contain letters")
        else:
            data = load()
            for category in data[username]["category"]:
                if category == choice:
                    return category


def create_task(name,end_date, responsible_person, description, category):
    data = load()
    task = Task(name, datetime.date.today().strftime("%d/%m/%Y"), end_date, responsible_person, description, category)
    if "tasks" not in data[responsible_person]:
        data[responsible_person]["tasks"]=[]
        data[responsible_person]["tasks"].append(task)
    else:
        data[responsible_person]["tasks"].append(task)
    save(data=data)
    return "Task Saved Successfully"

def all_users_tasks():
    data = load()
    all_user_tasks = []
    for user in data.keys():
          for task in data[user]["tasks"]:
            all_user_tasks.append(task)
    return all_user_tasks
    

def view_all_users_tasks():
    all_tasks = all_users_tasks()
    count = 1
    border()
    print()
    print("All Users Tasks:")
    print()
    if len(all_tasks) != 0:
        print("#: name, end date, category, responsible person".title())
        print()
        for task in all_tasks:
            print(f'{count}: {task}')
            count+=1
    else:
        print("No Tasks found in the Database!")

def border():
    print("----------------------------------------")

def edit_task():
    pass

def delete_task():
    pass

def search_task():
    pass

def filter_tasks():
    pass
