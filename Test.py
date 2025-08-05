#To do list
Tasks = []

def addTask(task):
    Tasks.append(str(task))

def ShowTask(task):
    for i in Tasks:
        print(i + "\n")

def RemoveTask(task):
    if task in Tasks:
        Tasks.remove(task)
        print(task + " successfully removed")
    else:
        print(task + " not found")

print('Please type 1 to add a task \ntype 2 to view to-do list \ntype 0 to remove task')
prompt = input()
if prompt == 1:
    addTask(prompt)
elif prompt == 2:
    ShowTask(prompt)
elif prompt == 0:
    RemoveTask(prompt)
else:
    print('Invalid Operation')