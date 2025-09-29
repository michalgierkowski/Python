contacts = {
    "John": 232323,
    "Richard": 38424}

while True:

    while True:
        try:
            selection = int(input("""    Available options:
            1. Add a new contact
            2. Search for contact
            3. Quit program                 
            Choose a option --->  """))
            break
        except ValueError:
            print("Please select the following (1 - 3)")
    
    if selection == 1:
        while True:
            name = input("Enter a name:  ").title()
            if not name.isalpha():
                print("That is not a valid field.")
            else:
                break
        while True:
            try:
                phone_number = int(input("Enter their phone number:  ").strip())
                break
            except ValueError:
                print("That is not a valid number.")
        contacts[name] = phone_number

    elif selection == 2:
        while True:
            search_name = input("Enter their name:  ").title()
            if not search_name.isalpha():
                print("That is not a valid name.")
            else:
                break

        if search_name in contacts:
            for name, number in contacts.items():
                print(f"{search_name}: {contacts[search_name]}")
        else:
            print(f"{search_name} doesn't exist.")
        
    else:
        print("Your current contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
        break