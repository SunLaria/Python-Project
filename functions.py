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
    data[user_name]={}
    data[user_name]={"tasks":[],"category":[]}
    save(data=data)
    return f"{user_name} user Created Succesffuly!"

def view_users():
    data = load()
    if len(data.keys()) > 0:
        print("----------------------------------------")
        return f"All Users:\n\n{', '.join(data.keys())}"
    else:
        print("----------------------------------------")
        return f"All Users:\n\nNo Users Found in Database"

def delete_user(user_name:str="default_username"):
    choice = input("Delete Confirmation y\\n: ")
    if choice == "y":
        data = load()
        if user_name in data.keys():
            del data[user_name]
            save(data=data)
            print()
            return f"{user_name} Deleted Succesffuly"
        else:
            print()
            return f"{user_name} Not Found"



def choose_user_task():
    while True:
        print()
        print(view_users())
        print()
        choice = input("Enter the responsible User for this task or [A]dd, [R]emove: ")
        print()
        if choice == "A":
            add_user = input("User Name to add: ")
            if add_user != "" or add_user.isspace() != False:
                try:
                    print(create_user(add_user))
                except:
                    print("Error Creating User")

        elif choice == "R":
            del_user = input("User Name to Delete: ")
            if del_user != "" or del_user.isspace() != False:
                try:
                    print()
                    print(delete_user(del_user))
                except:
                    print("Error Deleting User")
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
    print(f"{user_name} Category Created Succesffuly!")


def view_categories(username):
    data = load()
    if len(data[username]["category"]) != 0:
        print("----------------------------------------")
        return f"All {username} Categories:\n\n{', '.join(data[username]['category'])}"
    else:
        print("----------------------------------------")
        return f"All {username} Categories:\n\nNo Categories For this User"


def delete_category(user_name:str="default_username",category:str = "defualt_category"):
    choice = input("Delete Confirmation: y\\n")
    if choice == "y":
        data = load()
        if category in data[user_name]["category"]:
            data[user_name]["category"].remove(category)
            save(data=data)
            print()
            return f"{category} Deleted Succesffuly"
        else:
            print()
            return f"{category} Not Found"


def choose_category_task(username):
    while True:
        print(view_categories(username=username))
        print()
        choice = input("Enter the chosen category for this task or [A]dd, [R]emove: ")
        print()
        if choice == "A":
            add_categroy = input("Category Name to add: ")
            if add_categroy != "" or add_categroy.isspace() != False:
                try:
                    print(create_category(user_name=username,category=add_categroy))
                except:
                    print("Error Creating Category")
        elif choice == "R":
            del_categroy = input("Category Name to Delete: ")
            if del_categroy != "" or del_categroy.isspace() != False:
                try:
                    print()
                    delete_category(user_name=username,category=del_categroy)
                except:
                    print("Error Deleting User")
        else:
            data = load()
            for category in data[username]["category"]:
                if category == choice:
                    return category



def task_search():
    pass

def create_task(name,end_date, responsible_person, description, category):
    data = load()
    task = Task(name, datetime.date.today().strftime("%d/%m/%Y"), end_date, responsible_person, description, category)
    if "tasks" not in data[responsible_person]:
        data[responsible_person]["tasks"]=[]
        data[responsible_person]["tasks"].append(task)
    else:
        data[responsible_person]["tasks"].append(task)
    save(data=data)
    return "Task Saved Succesffuly"

def edit_task():
    pass

def delete_task():
    pass

def search_task():
    pass

def filter_tasks():
    pass
