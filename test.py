import crud
from myclass import Task
import random, datetime
from functions import startup


#testing load when no file exist, make sure no pickel file exits
try:
    crud.load()
    print("file exists")
except:
    print("file not exist")

# testing the save function
try:
    crud.save(["mm","nj"])
    print("file saved")
except:
    print("somthing went wrong")


#testing the load after save pickle creation
try:
    data = crud.load()
    print(f'file found with {data} in it')
except:
    print("somthing went wrong")


taskstitles = ["working with dad","walking the dog","doing laundry","baking","cooking dinner","working on a project"]
taskcategories = ["shop","home","dog"] 
names = ["ron","gal","moshe","shoval"]

def random_task():
    """random task creation"""
    return Task(name=random.choice(taskstitles), creation_date = datetime.date.today().strftime("%m/%d/%Y") ,end_date= datetime.date(day=20,month=3,year=2025).strftime("%m/%d/%Y"), responsible_person = random.choice(names),description="lorem impsum", category= random.choice(taskcategories))
    
# testing random_task function
try:
    print(random_task())
except:
    print("random task function went wrong")

#testing save random tasks in pickle file
def random_tasks_save_pickle(count:int = 10):
    """testing save random tasks in pickle file"""
    tasks = []
    for count in range(count):
        tasks.append(random_task())
    crud.save(data=tasks)

random_tasks_save_pickle()

#viewing random tasks:
tasks = crud.load()
for task in tasks:
    print(task)


#test delete function
# delete function
print()
data = crud.load()
task = data[0]
print(f"trying to delete {task}")
crud.delete_test(task=data[0],data=data)
crud.save(data=data)
if task == data[0]:
    print("delete went wrong")
else:
    print("delete went good")