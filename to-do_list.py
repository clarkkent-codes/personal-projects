tasks = ["Practice1", "Practice2", "Practice3", "Practice4"]

def add_task():
    add_task = str(input("\nAdd Task: "))
    tasks.append(add_task)

def update_task():
    print("Task: " + "\n".join(tasks))
    task_index = int(input("\nUpdate Task [1/9]: "))
    print(tasks[task_index - 1])
    updated_task = str(input("New Task: "))
    tasks[task_index - 1] = updated_task 
    print("Updated Task: ", tasks[task_index - 1])

def remove_task():
    remove_task = int(input("\nRemove Task [1/9]: "))
    remove_task = remove_task - 1
    removed_item = tasks.pop(remove_task)
    print("Removed: ", removed_item)

def view_task():
    print("\nTask:\n" + "\n".join(tasks))

while True:
    print("[0] Exit | [1] Add Task | [2] Update Task | [3] Remove Task | [4] View Task")
    choice = int(input("What do you want to do?: "))

    if choice == 0:
        print("\nDone Listing Task")
        break

    elif choice == 1:
        add_task()

    elif choice == 2:
        update_task()

    elif choice == 3:
        remove_task()

    elif choice == 4:
        view_task()
        
    elif choice not in [0, 1, 2, 3, 4]:
        print("\nChoice is out of index!")
        continue

    else:
        break