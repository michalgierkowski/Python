import sys

# add to do
# view to do
# remove to do


def to_do_list():
    tasks = []
    return tasks


def menu_page():

    print(""" ------ Menu Page ------
    
    1. Add a new task          
    2. View tasks
    3. Remove a task
    4. Clear all tasks
    5. Quit
    """)

    try:
        user_selection = int(input("Enter your option -->  ").strip())      # when polishing do try, except
        if user_selection > 5:
            print("Select the following options (1 - 5).")
        return user_selection
    except ValueError:
        print("Enter a numeric value")


def add_task(tasks):
    while True:
        user_task = input("Enter a new task:  ").strip()
        
        if user_task == "":
            print("Task cannot be empty!")
        if user_task in tasks:
            print(f"{user_task} is already added!")
        else:
            tasks.append(user_task)
            return tasks
        


def view_tasks(tasks):
    
    index = 0
    found = False

    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        found = True

    if found:
        for task in tasks:
            index += 1
            print(f" {index}. {task}")


def remove_task(tasks):


    try:
        user_input = int(input("Enter task number to remove:  ").strip())
        index = user_input - 1
        removed_task = tasks.pop(index)
        print(f"Removed task: {removed_task}")
    except ValueError:
        print("Enter a numeric value")
    except IndexError:
        print(f"Number {user_input} does not exist.")
    

def clear_tasks(tasks):
    
    print("All tasks cleared!")
    return tasks.clear()
    

def quit():
    print("Goodbye!")
    sys.exit()


def run_program():


    tasks = to_do_list()

    while True:
        menu = menu_page()

        if menu == 1:
            add_task(tasks)
        elif menu == 2:
            view_tasks(tasks)
        elif menu == 3:
            remove_task(tasks)
        elif menu == 4:
            clear_tasks(tasks)
        elif menu == 5:
            quit()


run_program()
            