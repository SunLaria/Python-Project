from crud import save,load, edit,delete, search
from myclass import Task
import datetime
from dateutil.relativedelta import relativedelta


def startup():
    """Starting up the app, verifying there is an saved pickle file, if not creating one"""
    try:
        load()
        print("Database found")
    except:
        save(data={})
        print("Database Created")
    return True

def verify_uppercase(string:str):
    """verify user input uppercase"""
    if string.istitle() != True and string.isalpha() == True:
        return string.title()
    else:
        return string


def create_user(user_name:str = "defualt_username"):
    """creates a user in database"""
    data = load()
    user_name = verify_uppercase(user_name)
    if user_name not in data.keys():
        data[user_name]={}
        data[user_name]={"tasks":[],"category":[]}
        save(data=data)
        return f"{user_name} user Created Successfully!"
    else:
        return f"{user_name} User Already Exists"

def view_users():
    """view all users in database"""
    data = load()
    border()
    print()
    if len(data.keys()) > 0:
        return f"All Users:\n\n{', '.join(data.keys())}"
    else:
        return f"All Users:\n\nNo Users Found in Database"

def delete_user(user_name:str="default_username"):
    """delete user from database """
    user_name = verify_uppercase(user_name)
    choice = input("Delete Confirmation Y\\N: ")
    choice = verify_uppercase(choice)
    if choice == "Y":
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
    """users menu - return/add/remove"""
    while True:
        print(view_users())
        print()
        choice = input("Enter the responsible User for this task or [A]dd, [R]emove: ")
        choice = verify_uppercase(choice)
        print()
        if choice == "A":
            add_user = input("User Name to add: ")
            add_user = verify_uppercase(add_user)
            if add_user != "" and add_user.isspace() != True and add_user.isalpha() == True:
                print(create_user(add_user))
            else:
                print("Eror - User can only contain letters")

        elif choice == "R":
            del_user = input("User Name to Delete: ")
            del_user = verify_uppercase(del_user)
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
    """creates a category specified to a user"""
    data = load()
    user_name = verify_uppercase(user_name)
    category = verify_uppercase(category)
    data[user_name]["category"].append(category)
    save(data=data)
    return f"{category} Category Created Successfully!"


def view_categories(username:str = "defualt_username"):
    """view specified user categories"""
    data = load()
    username = verify_uppercase(username)
    border()
    print()
    if len(data[username]["category"]) != 0:
        return f"All {username} Categories:\n\n{', '.join(data[username]['category'])}"
    else:
        return f"All {username} Categories:\n\nNo Categories For this User"


def delete_category(user_name:str="default_username",category:str = "defualt_category"):
    """delete category from specified user"""
    user_name = verify_uppercase(user_name)
    category = verify_uppercase(category)
    choice = input("Delete Confirmation: Y\\N: ")
    choice = verify_uppercase(choice)
    if choice == "Y":
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

def choose_category_task(username:str = "defualt_username"):
    """user category menu - return/add/remove"""
    username = verify_uppercase(username)
    while True:
        print(view_categories(username=username))
        print()
        choice = input("Enter the chosen category for this task or [A]dd, [R]emove: ")
        choice = verify_uppercase(choice)
        print()
        if choice == "A":
            add_categroy = input("Category Name to add: ")
            add_categroy = verify_uppercase(add_categroy)
            if add_categroy != "" and add_categroy.isspace() != True and add_categroy.isalpha() == True:
                add_categroy = verify_uppercase(add_categroy)
                print(create_category(user_name=username,category=add_categroy))
            else:
                print("Eror - Category can only contain letters")

        elif choice == "R":
            del_categroy = input("Category Name to Delete: ")
            del_categroy = verify_uppercase(del_categroy)
            if del_categroy != "" and del_categroy.isspace() != True and del_categroy.isalpha() == True:
                del_categroy = verify_uppercase(add_categroy)
                print()
                print(delete_category(user_name=username,category=del_categroy))
            else:
                print("Eror - Category can only contain letters")
        else:
            data = load()
            for category in data[username]["category"]:
                if category == choice:
                    return category

def end_date_define(creation_date:tuple,num:int=0,choice:str="default"):
    """end date definer"""
    if choice == "D":
        return creation_date + relativedelta(days=int(num))
    elif choice == "M":
        return creation_date + relativedelta(months=int(num))
    elif choice == "Y":
        return creation_date + relativedelta(years=int(num))


def all_users_tasks():
    """return all users tasks"""
    data = load()
    all_user_tasks = []
    for user in data.keys():
          for task in data[user]["tasks"]:
            all_user_tasks.append(task)
    return all_user_tasks
    

def view_all_users_tasks(tasks_list:list="all_tasks"):
    """view all users tasks"""
    count = 1
    print("All Users Tasks:")
    print()
    if len(tasks_list) != 0:
        print("#: name, end date, category, responsible person".title())
        print()
        for task in tasks_list:
            print(f'{count}: {task}'.title())
            count+=1
    else:
        print("No Tasks found in the Database!")

def view_sorted_tasks(tasks_list:list="all_tasks:", sort_word:str="responsible_person"):
    """view sorted tasks"""
    tasks_list.sort(key = lambda x: getattr(x, sort_word)[0])
    count = 1
    print(f"All Users Tasks Sorted By {sort_word}:".title())
    print()
    if len(tasks_list) != 0:
        print("#: name, end date, category, responsible person".title())
        print()
        
        for task in tasks_list:
            print(f'{count}: {task}'.title())
            count+=1
    else:
        print("No Tasks found in the Database!")


def border():
    """print border"""
    print("----------------------------------------")


def edit_task(task:object = "task", choice:str="defualt"):
    """edit specified task"""
    if choice == "End Date":
        return 'Use Extend Feature'
    elif choice == "Responsible Person":
        data = load()
        cache_task = task
        delete(task=cache_task,data=data)
        save(data=data)
        new_user = choose_user_task()
        data = load()
        edit(task=cache_task,key="responsible_person",new_value=new_user)
        data[new_user]["tasks"].append(cache_task)
        save(data=data)
        return f"{choice} Edit Went Successfully"
    elif choice == "Category":
        data = load()
        cache_task = task
        delete(task=cache_task,data=data)
        save(data=data)
        new_category = choose_category_task(cache_task.responsible_person)
        data=load()
        edit(task=cache_task,key="category",new_value=new_category)
        data[cache_task.responsible_person]["tasks"].append(cache_task)
        save(data=data)
        return f"{choice} Edit Went Successfully"
        
    else:
        new_value = input("Enter a new value: ")
        new_value = verify_uppercase(new_value)
        if new_value != "" and new_value.isspace() == False:
            data = load()
            cache_task = task
            delete(task=cache_task,data=data)
            keys = {"Name":"name","End Date":"end_date","Description":"description"}
            edit(task=cache_task,key=keys[choice],new_value=new_value)
            data[cache_task.responsible_person]["tasks"].append(cache_task)
            save(data=data)
            return f"{choice} Edit Went Successfully"
        else:
            return 'Value Cannot Be Empty'

def delete_task(task:object = "task"):
        """delete specified task"""
        data = load()
        delete(task=task, data=data)
        save(data=data)
        return 'Task Deleted Successfully'

def extend_task(task:object = "task"):
    """extend specified task"""
    while True:
        border()
        print()
        date_keys = {"Y":"Years","D":"Days","M":"Months"}
        date_key = input("Extend Task Period:\n\n[D]ays, [M]onthes, [Y]ears , [B]ack To Menu: ")
        date_key = verify_uppercase(date_key)

        if date_key != "" and date_key.isspace() == False:
            if date_key == "B":
                break
            elif date_key in date_keys.keys():
                print()
                number= input(f"How Many {date_keys[date_key]}: ")
                if number.isdigit() == True and int(number) > 0:
                    data = load()
                    cache_task = task
                    delete(task=task, data=data)
                    edit(task=cache_task,key="end_date",new_value=end_date_define(creation_date=cache_task.end_date,num=number,choice=date_key))
                    data[cache_task.responsible_person]["tasks"].append(cache_task)
                    save(data=data)
                    return 'Task Extend Successfully'