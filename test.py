from crud import load,save
from myclass import Task
import random, datetime


#testing load when no file exist, make sure no pickel file exits
try:
    load()
except:
    print("file not exist")

# testing the save function
try:
    save(["mm","nj"])
except:
    print("somthing went wrong")


#testing the load after save pickle creation
try:
    data = load()
    print(f'file found with {data} in it')
except:
    print("somthing went wrong")


taskstitles = ["working with dad","walking the dog","doing laundry","baking","cooking dinner","working on a project"]
taskcategories = ["shop","home","dog"] 
names = ["ron","gal","moshe","shoval"]

def randomtask():
    """random task creation"""
    # function to create random tasks
    return Task(name=random.choice(taskstitles), creation_date = datetime.date.today().strftime("%m/%d/%Y") ,end_date= datetime.date(day=20,month=3,year=2025).strftime("%m/%d/%Y"), responsible_person = random.choice(names),description="lorem impsum", category= random.choice(taskcategories))
    
# testing randomtask function
try:
    print(randomtask().taskinfo())
except:
    print("random task function went wrong")

#testing save random tasks in pickle file
def random_tasks_save_load_pickle(count:int = 10):
    """testing save random tasks in pickle file
"""
    tasks = []
    for count in range(count):
        tasks.append(randomtask())
    try:
        save(tasks)
    except:
        print("save went wrong")
    try:
        load()
        for task in tasks:
            print(task.taskinfo())
    except:
        print("load went wrong")

# random_tasks_save_load_pickle()

