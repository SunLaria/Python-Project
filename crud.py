import pickle
from myclass import Task
import datetime

def save(data,file:str = "data.pickle"):
    """save data to pickle file"""
    with open(file,"wb") as f:
        pickle.dump(data,f)


def load(file:str = "data.pickle"):
    """Loads a pickle file and return data"""
    with open(file,"rb") as f:
        data = pickle.load(file=f)
    return data

def search(task:object="default_task",data:dict="data"):
    """search and return the task object"""
    for user in data.keys():
        for user_task in data[user]["tasks"]:
            if user_task.name == task.name:
                return user_task

def delete(task:object="default_task",data:dict="data"):
    """search and delete a task from specifid data"""
    for user in data.keys():
          for user_task in data[user]["tasks"]:
            if user_task.name == task.name:
                 data[user]["tasks"].remove(user_task)
                 return "Deleted"

def delete_test(task:object="default_task",data:list="data"):
    """search and delete a task from specifid data"""
    for task in data:
            data.remove(task)
            return "Deleted"


def edit(task:object="default_task",key:str = "default_key",new_value:str = "default_value"):
    """edit task atteibute"""
    setattr(task,key,new_value)
    return "Edited"


def create_task(name:str,end_date:tuple, responsible_person:str, description:str, category:str):
    """create task and save to pickle"""
    data = load()
    task = Task(name, datetime.date.today(), end_date, responsible_person, description, category)
    if "tasks" not in data[responsible_person]:
        data[responsible_person]["tasks"]=[]
        data[responsible_person]["tasks"].append(task)
    else:
        data[responsible_person]["tasks"].append(task)
    save(data=data)
    print()
    return "Task Saved Successfully"
