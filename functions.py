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

def create_user(user_name:str="default_username"):
    """creates a user"""
    try:
        data = load()
        data[user_name]={}
        data[user_name]["category"]=[]
        data[user_name]["tasks"]=[]
        save(data=data)
        return f"{user_name} User Created Succesffuly!"
    except:
        return "Database Not Found, Restart the menu"

def view_users():
    data = load()
    print("All Users: ")
    print()
    if len(data.keys()) > 0:
        return ", ".join(data.keys())
    else:
        return "No Users Found In Database"

def delete_user(user_name:str="default_username"):
    choice = input("Delete Confirmation: y\\n")
    if choice == "y":
        data = load()
        try:
            del data[user_name]
            save(data=data)
            print(f"{user_name} was deleted Succesffuly")
        except:
            print(f"{user_name} Not Found")

def choose_user_task():
    print(view_users())
    username = input("Enter your Responsible User for this task:")
    data = load()
    for user in data.keys():
        if username == user:
            return user



def create_category(user_name:str = "defualt_username", category:str="default_category"):
    """creates a user"""
    try:
        data = load()
        data[user_name]["category"].append(category)
        save(data=data)
        print(f"{user_name} Category Created Succesffuly!")
    except:
        print("Database Not Found, Restart the menu")

def view_categories(username):
    data = load()
    print(f"All {username} Categories: ")
    print(", ".join(data[username]["category"]))

def delete_category(user_name:str="default_username",category:str = "defualt_category"):
    choice = input("Delete Confirmation: y\\n")
    if choice == "y":
        data = load()
        try:
            if category in data[user_name]["category"]:
                del data[user_name]["category"]
                save(data=data)
                print(f"{category} Deleted Succesffuly")
        except:
            print(f"{category} Not Found")

def choose_category_task(username):
    view_categories(username=username)
    choice = input("Enter the chosen category for this task or [A]dd, [R]emove: ")
    if choice == "A":
        add_categroy = input("Category Name to add: ")
        if add_categroy != "" or add_categroy.isspace() != True:
            create_category(user_name=username,category=add_categroy)
    elif choice == "R":
        del_categroy = input("Category Name to add: ")
        if del_categroy != "" or del_categroy.isspace() != True:
            delete_category(user_name=username,category=del_categroy)
    else:
        data = load()
        for category in data[username]["category"]:
            if category == choice:
                return category
        else:
            print("Category Not found")



def task_search():
    pass

def create_task(name,end_date, responsible_person, description, category):
    data = load()
    task = Task(name, datetime.date.today().strftime("%d/%m/%Y"), end_date, responsible_person, description, category)
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
