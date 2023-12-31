import csv
import os 
def display_menu():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Simple To-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as complete")
    print("4. Clear Completed Tasks")
    print("5. Exit")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
def view_tasks():
    with open("tasks.csv","r", newline="") as file:
        reader =csv.reader(file) 
        tasks= list(reader)
        if not tasks:
            print("No tasks found")
        else :
            for index,tasks in enumerate(tasks,start=1):
                print(f"{index}. {tasks[0]}")
def add_task():
    task_name= input("Enter the task: ")
    with open("tasks.csv","a", newline="") as file:
        writer= csv.writer(file)
        writer.writerow([task_name])
        print("Task added successfully!")
def mark_task_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        with open("tasks.csv", "r", newline="") as file:
            reader = csv.reader(file)
            tasks = list(reader)
            if 0 <= task_index < len(tasks):
                completed_task = tasks[task_index]
                if not completed_task[0].endswith("(completed)"):
                    completed_task[0] += " (completed)"
                    with open("tasks.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(tasks)
                    print(f"Task '{completed_task[0]}' marked as completed.")
                else:
                    print("Task is already marked as completed.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def clear_completed_tasks():
    with open("tasks.csv", "r", newline="") as file:
        reader = csv.reader(file)
        tasks = list(reader)
        incomplete_tasks = [task for task in tasks if not task[0].endswith("(completed)")]
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(incomplete_tasks)
    print("Completed tasks cleared.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            clear_completed_tasks()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()                  
