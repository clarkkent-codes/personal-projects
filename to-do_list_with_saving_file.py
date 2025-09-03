import os

def create_file():
    try:
        with open("todolist.txt", "x") as f:
            f.write("")
    except FileExistsError:
        print("File already exist")

def append_task(task):
    with open("todolist.txt", "a") as f:
        f.write(task + "\n")

def read_file():
    if os.path.exists("todolist.txt"):
        f = open("todolist.txt", "r")
        for line in f:
            print(line.strip("\n"))
    else:
        print("File does not exist")

def delete_file():
    if os.path.exists("todolist.txt"):
        os.remove("todolist.txt")
    else:
        print("File does not exist")

create_file()

while True:
    print("[0] Exit | [1] Add Task | [2] View Task | [3] Delete File")
    choice = int(input("Type the number of what you want to do: "))

    if choice == 0:
        print("\nDone Listing Task")
        break

    elif choice == 1:
        task = str(input("Add Task: "))
        append_task(task)
    
    elif choice == 2:
        read_file()
    
    elif choice == 3:
        answer = str(input("Are you sure you want to delete the file? [y/n]: ")).lower()
        if answer == 'y':
            delete_file()
            print("\nSuccessfully deleted!")
            continue
        else:
            break

    elif choice not in [0, 1, 2, 3]:
        print("\nChoice is out of index!")
        continue

    else:
        print("Done adding and editing task")
        break