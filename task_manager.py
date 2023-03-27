#=====importing libraries===========
from datetime import datetime
from datetime import date

#=====USEFULE GLOBAL VARIABLES=====
today = date.today()

tasks = open("tasks.txt", "r")

users = open("user.txt", "r")

task_data = tasks.readlines()

user_data = users.readlines()

admin_menu = '''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    g - generate reports
    s - statistics
    e - Exit
    \n:'''

standard_menu = '''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    \n: '''

#=====[FUNCTIONS]===========

#-----Register a new user-----
def reg_user():
    # Allows the user to add a new user
    users = open("user.txt", "r")
    new_username = input("Create a username: ")
    new_password = input("Create password: ")
    new_password1 = input("Confirm password: ")
    if new_password != new_password1:
        print("Passwords dont match, restart")
        reg_user()
    else:
        if len(new_password) <= 6:
            print("Password too short, restart:")
            reg_user()
        elif new_username in users:
            print("Username exists")
            reg_user()
        else:
            users = open("user.txt", "a")
            users.write("\n" + new_username + ", " + new_password)

#-----Add a new task-----
def add_task():
    # Function lets the user add a new task and appends appropriate txt file
    for line in task_data:
            split_task = line.split(", ")
            print("-----[Add a new task]-----")
            new_user = input("Username: ")
            new_task = input("Task: ")
            new_description = input("Description: ")
            new_date = input("Assigned date: ")
            new_due_date = input("Due Date: ")
            taskadd = open("tasks.txt", "a")
            taskadd.write(f"\n{new_user}, {new_task}, {new_description}, {new_date}, {new_due_date}, No")
            print("New task added:\n")
            print(f"Assigned to: {new_user}\n")
            print(f"Task: {new_task}\n")
            print(f"Description: {new_description}\n")
            print(f"Assigned date: {new_date}\n")
            print(f"Due date: {new_due_date}\n")
            print(f"Is completed: No\n")
            taskadd.close()
            break

#-----View all tasks-----
def view_all():
    # Loop through and display all tasks cleanly
    for pos, line in enumerate(task_data, 1):
        split_task = line.split(", ")
        output = f"_____[{pos}]_____\n"
        output += "\n"
        output += f"Assigned to: {split_task[0]}\n"
        output += f"Task: {split_task[1]}\n"
        output += f"Description: {split_task[2]}\n"
        output += f"Assigned date: {split_task[3]}\n"
        output += f"Due date: {split_task[4]}\n"
        output += f"Is completed: {split_task[5]}\n"
        output += "_____________\n"
        print(output)
    # Choose a task to view:
    while True:
        task_choice = int(input("Select a task by number or type '-1'to return to the main menu"))-1
        # Exit if -1 selected
        if task_choice == "-1":
            return 
        elif task_choice <= -2 or task_choice > len(task_data):
            print("You have selected an invalid option, try again.")
            continue
        edit_data = task_data[task_choice] 
        break

    # Show selected task
    edit_data_list = edit_data.split(", ")
    print("_______ Selected Task_______\n")    
    print(f"Task number: {task_choice +1}")
    print(f"Assigned to: {edit_data_list[0]}")
    print(f"Task: {edit_data_list[1]}")
    print(f"Description: {edit_data_list[2]}")
    print(f"Assigned Date: {edit_data_list[3]}")
    print(f"Due Date: {edit_data_list[4]}")
    print(f"Is Completed: {edit_data_list[5]}")

    # Give the user options for edit etc
    while True:
        output = f"_________ SELECT AN OPTION_________ \n"
        output += "1 Edit Due Date \n"
        output += "2 Mark as completed \n"
        output += "3 Change user task is assigned to \n"
        output += "_______________\n"

        choice = int(input(output))

        if choice <= 0 or choice >= 4:
            print("You have selected an invalid option, try again.")
            continue

        if choice == 1:
            print("Please enter a new due date format day month year: \n")
            split_data = edit_data.split(", ")
            split_data[4] = input("New date: ")
            new_data = ", ".join(split_data)
            task_data[task_choice] = new_data

        elif choice == 2:
            print("File updated, task marked as complete")
            split_data = edit_data.split(", ")
            split_data[-1] = "Yes\n"
            new_data = ", ".join(split_data)
            task_data[task_choice] = new_data

        elif choice == 3:
            print("Assign a new user to this task \n")
            split_data = edit_data.split(", ")
            split_data[0] = input("New user: ")
            new_data = ", ".join(split_data)
            task_data[task_choice] = new_data
            print("New user assigned")
            
        tasks_write = open("tasks.txt", "w")
        for line in task_data:
            tasks_write.write(line) 
        tasks_write.close()
        break      


#-----View my tasks-----
def view_mine():
    # Lets the user view their tasks
    for pos, line in enumerate(task_data, 1):
        split_task = line.split(", ")
        output = f"_____[{pos}]_____\n"
        output += "\n"
        output += f"Assigned to: {split_task[0]}\n"
        output += f"Task: {split_task[1]}\n"
        output += f"Description: {split_task[2]}\n"
        output += f"Assigned date: {split_task[3]}\n"
        output += f"Due date: {split_task[4]}\n"
        output += f"Is completed: {split_task[5]}\n"
        output += "_____________\n"
        if username == split_task[0]:
            print(output)

def reports():
    # Function generates reports and exports to txt files
     # ----------TASK REPORT----------
        task_overview = open("task_overview.txt", "w+") 
        # Number of tasks
        task_number = len(task_data)
        # Count complete and incomplete tasks
        task_no = 0
        task_yes = 0
        # Count for overdue tasks
        overdue = 0
        for line in task_data:
            # Number of incomplete and overdue tasks
            data = line.split(", ")
            date = (datetime.strptime(data[4], "%d %b %Y").date())
            if date < today and data[-1] == "No\n":
                 overdue += 1
            # Count complete and incomplete tasks
            if data[-1] == "No\n":
                task_no += 1
            elif data[-1] == "Yes\n":
                task_yes += 1
        # Percentage of tasks that are incomplete
        percentage_incomplete = (task_no / task_number) *100
        # Percentage of tasks that are overdue
        percentage_overdue = (overdue / task_number) * 100
        output = "----------TASK OVERVIEW----------\n"
        output += f"Number of tasks: {task_number}\n"
        output += f"Number of completed tasks: {task_yes}\n"
        output += f"Number of incomplete tasks: {task_no}\n"
        output += f"Number of overdue tasks: {overdue}\n"
        output += f"Percentage of incomplete tasks: {percentage_incomplete}%\n"
        output += f"Percentage of overdue tasks: {percentage_overdue}%\n"
        task_overview.write(output)
        task_overview.close()

    # ----------USER REPORT ----------
        user_overview = open("user_overview.txt", "w+")
        user_number = len(user_data)
        user_tasks = {}
        user_completed = {}
        user_incomplete= {}
        user_overdue = {}

        for line in task_data:
            data = line.split(", ")
            # add users to dictionaries
            user_tasks[data[0]] = 0
            user_completed[data[0]] = 0
            user_incomplete[data[0]] = 0
            user_overdue[data[0]] = 0

        for line in task_data:
            # Number of tasks completed / incomplete added to dictionary
            data = line.split(", ")
            user_tasks[data[0]] += 1
            if data[-1] == "No\n" or data[-1] == "No":
                user_incomplete[data[0]] += 1
            elif data[-1] == "Yes\n" or data[-1] == "Yes":
                user_completed[data[0]] += 1

            date = (datetime.strptime(data[4], "%d %b %Y").date())    
            if data[-1] == "No\n" or data[-1] == "No" and date < today:
                user_overdue[data[0]] += 1

        output = "----------USER OVERVIEW----------\n"
        output += f"Total number of registered users: {user_number}\n"
        output += f"Total number of tasks created: {task_number}\n"
        # Add each users tasks
        for user in user_tasks:
            output += f"\n----------{user.upper()}----------\n"
            output += "Overview:\n"
            output += f"Tasks assigned: {user_tasks[user]}\n"
            output += f"% of overall tasks assigned to user: {(user_tasks[user]/task_number) * 100}%\n"
            output += f"Tasks completed: {(user_completed[user]/user_tasks[user]) * 100}%\n"
            output += f"Tasks not completed: {(user_incomplete[user]/user_tasks[user]) * 100}%\n"
            output += f"Overdue tasks: {(user_overdue[user]/user_tasks[user]) * 100}%\n"

        user_overview.write(output)
        user_overview.close()

def read_reports():
    # Function reads generated reports from a txt file
    print("\n\nUser report:\n\n")
    user_report = open("user_overview.txt", "r")
    user_report_contents = user_report.read()
    print(user_report_contents)

    print("Task report:\n\n")
    task_report = open("task_overview.txt", "r")
    task_report_contents = task_report.read()
    print(f"{task_report_contents}\n\n")

#====Login Section====
# Not in an app as the username is global

# Placeholder for while loop
login = False

while login == False:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for line in user_data:
        login_info = line.strip().split(", ")
        if username == login_info[0] and password == login_info[1]:
            print(f"Logged in as {login_info[0]}\n")      
            login = True     
    if login == False:
        print("incorrect credentials, try again.\n")

#-----MENU-----
while True:
    # admin menu
    if username == "admin":
        menu = input(admin_menu).lower()
    # Normal user menu
    else:
         menu = input(standard_menu).lower()

    if menu == 'r':
        # Check to see if admin otherwise don't allow to add new users
        if username == "admin":
            reg_user()
        else:
            print("\n-----[Error, only the admin may register new users.]-----\n")

    elif menu == 'a':   
        # Add a new task 
        add_task()

    elif menu == 'va':
        # Display all tasks with task numbers
            view_all()
            
        # Update global variables to adjust for file edits:
            tasks.close()
            tasks = open("tasks.txt", "r")

            users.close()
            users = open("user.txt", "r")

            task_data = tasks.readlines()

            user_data = users.readlines()

    elif menu == 'vm':
        # View tasks assigned to the logged in user 
         view_mine()

    # Reports only available for admin so double check before showing:
    elif menu == "g" and username == "admin":
        reports()
        print("User and task reports generated")

    # Statistics are only for admin so check before showing            
    elif menu == 's' and username == "admin": 
        reports()
        read_reports()


    # Exit the loop
    elif menu == 'e':
        print('Goodbye.')
        users.close()
        tasks.close()
        exit()

    # Catch all for incorrect selections
    else:
        print("You have made a wrong choice, Please Try again")
