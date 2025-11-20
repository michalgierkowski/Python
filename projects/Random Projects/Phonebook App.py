

def phone_numbers_details():

    names = {
        "John":"3291",
        "Richard":"1921",
        "Elise":"0821",
        "Mark":"2814"
    }
    
    return names

def menu():

    print(""" 
          1. Look up an number
          2. Add a new contact
          3. Update a number
          4. Show all contacts
          5. Exit """)
    print()

    while True:
        choice = input("Select an option (1-5) ---->  ").strip()
        if choice in {"1","2","3","4","5"}:             # use set here as it's faster for "in" checks 
            return choice                               # if choice in sets return the choice
        print("Please enter a valid number (1-5)")      # if condition not met, print this and restart loop

   

def look_up_number(names):

    users_name = input("Enter a name >  ").title().strip()

    if users_name in names:      # if users input name is key in names dictionary (is True)
        print(f"{users_name}'s phone number: {names[users_name]}")   # names[user_name] finds the value for the key "user_name"
        return names                                                 # if this condition is met return the dict            
    else:
        print(f"{users_name} is not found")
                
    # no need of while loop here, as it can return to menu and let user select again
    
def add_new_contact(names):

    while True:   # only need one loop
        users_name = input("Enter a name >  ").title().strip()
        users_number = input("Enter their number:  ").strip()
                    
        if not users_name.isalpha():
            print("Non-alphabetic characters are not allowed within a name")
            continue                                                        # no need for "else" as continue restarts the loop if this condition is met
                    
        if not users_number.isdigit():
            print("Non-numeric characters are not allowed within a phone number")
            continue                                                        # same as here
            

        confirmation = input(f"Name: {users_name} - Phone number: {users_number} correct? (y/n):  ").lower().strip()
                
        if confirmation == "y":
            names[users_name] = users_number
            return names
                    

def update_number(names):

    user = input("Enter the name to update >  ").title().strip()

    if not user in names:
        print("Not found")
        return names      # if not found return to menu
    
    number = input("Enter a new number -->  ").strip()    # if name was found
    if not number.isdigit():
        print("Invalid number!")
        return names        # return back to menu
    
    confirm = input(f"Update {user} to {number}? (y/n):  ").lower().strip()
    if confirm == "y":
        names[user] = number
        print(f"{user}'s number updated")
    return names        # always return updated dict

            

def show_contacts(names):

    for name, number in names.items():     # unpacked it here to make it look cleaner 
            print(f"{name} - Phone number: {number}")


def exit_program():
    print("Bye!")


                
def menu_choice(user_input, names):

    if user_input == "1":
        return look_up_number(names)
    
    elif user_input == "2":
        return add_new_contact(names)
    
    elif user_input == "3":
        return update_number(names)
    
    elif user_input == "4":
        return show_contacts(names)






def run_program():
                    

    names = phone_numbers_details()     # outside of loop to allow new key/values to be stored
    
    while True:
        
        choice = menu()
        menu_choice(choice,names)
        
        if choice == "5":
            break


run_program()





# return in loop = only when a certain happens
# return out loop = once loop finishes
# remember to keep it simple and readable