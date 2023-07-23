from crud import save,load
from myclass import Task
import datetime

def startup():
    """Starting up the app, verifying there is an saved pickle file, if not creating one"""
    try:
        data = load()
        print("Database found")
    except:
        save(data=[])
        print("Database Created")
    return True

# print(startup())

def create_task(name,end_date, responsible_person, description, category):
    return Task(name, datetime.date.today().strftime("%m/%d/%Y"), end_date, responsible_person, description, category)

def edit_task():
    pass

def delete_task():
    pass

def search_task():
    pass

def filter_tasks():
    pass
