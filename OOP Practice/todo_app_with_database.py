import sqlite3

class TaskManager:
    def __init__(self):
        self.connection = sqlite3.connect("taskmanager.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    #create table = task_data
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS task_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                completed TEXT NOT NULL
            )
        ''')
        self.connection.commit()
    
    def add_task(self, title, description, completed):
        self.cursor.execute(
            "INSERT INTO task_data(title, description, completed) VALUES (?, ?, ?)",
            (title, description, completed)
        )
        self.connection.commit()
    
    def update_task(self, task_id, completed):
        self.cursor.execute(
            "UPDATE task_data SET completed = ? WHERE id = ?",
            (completed, task_id)
            )
        self.connection.commit()
        print("Task updated successfully!")
    
    def delete_task(self, task_id):
        self.cursor.execute(
            "DELETE FROM task_data WHERE id = ?",
            (task_id,)
            )
        self.connection.commit()
        print("Task deleted successfully!")

    def list_task(self):
        self.cursor.execute("SELECT * FROM task_data")
        results = self.cursor.fetchall()
        if not results:
            print("No task found.")
        else:
            for result in results:
                print(result)

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = 'No'

def main_app():
    print("─────────────────────────TASK MANAGER──────────────────────")
    print("| [0] Exit | [1] Add | [2] Update | [3] Delete | [4] Show |")
    print("───────────────────────────────────────────────────────────")
    while True:
        choice = int(input("Choice: "))
        if choice == 0:
            print("Done editing task.")
            break
        elif choice == 1:
            title = str(input("Add Title: "))
            description = str(input("Add Description: "))
            task = Task(title, description)
            manager.add_task(task.title, task.description, task.completed)

        elif choice == 2:
            task_id = int(input("Enter Task ID: "))
            completed = input("Completed? [Yes/No]: ")
            manager.update_task(task_id, completed)

        elif choice == 3:
            manager.list_task()
            task_id = int(input("Enter Task ID: "))
            confirmation = str(input(f"Do you really want to delete Task ID: {task_id} [y/n]?")).lower()
            if confirmation == 'y':
                manager.delete_task(task_id)
            else:
                return
                
        elif choice == 4:
            manager.list_task()
        
        elif choice not in (0, 1, 2, 3, 4):
            print("Choice is out index.")
            
        else:
            break

manager = TaskManager()
if __name__ == "__main__":
    main_app()