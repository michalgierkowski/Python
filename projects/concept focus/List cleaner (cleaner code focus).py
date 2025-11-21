# list to store user values
values = []

# A function that checks our tuple and looks for matches
# if no match --> returns a output
# if a match is found --> returns users input which goes to the next "checks"
def checkUserInput(user):
    if user not in ("1","2","3"):
        return print(f"'{user}' is not from the following (1-3).")
    else:
        return user

while True: 
    userInput = input("Choose from the following: \n" 
    "1. Store a word \n"
    "2. Store a number \n"
    "3. View next page \n"
    "Enter here:  ")

    # calling up our function
    checkUserInput(userInput)

    if userInput == "1":
        # a string can involve numeric or alphabetical units
        text = input("Enter a word of your choice:  ")
        print(f"'{text}' has been successfully stored.")
        values.append(text)

    elif userInput == "2":
        # looping till user enters a correct value
        while True:
            number = int(input("Enter a number between 1 and 10:  "))
            if 10 >= number >= 1:
                print(f"'{number}' has been successfully stored. ")
                values.append(number)
                break    
            else:
                print(f"'{number}' is not within the range. Try again.")
        
    # Previously I had "else: break" but this doesn't work
    # As we need to specific what we are waiting for which is '3'    
    elif userInput == "3":
        break

while True: 
    userRequest = input("Would you like to:\n" 
        "1. View only words?\n"
        "2. View only numbers?\n"
        "3. View your list?\n"
        "Select your option -->   ")

    # calling our function again
    checkUserInput(userRequest)

    if userRequest == "1":
        print("Your list of words:")
        for string in values:
            if isinstance(string, int):
                values.remove(string)
            print(f"- {string}") 
        break
    

    # finish this + new list to insert values from ascending order
    elif userRequest == "2":
        for index in range(len(values) - 1, -1, -1):
            if isinstance(values[index], str):
                values.pop(index)         #.pop() is for removing a element based on it's position     



            
    elif userRequest == "3":
        print("Your list:")
        for value in values:
            print(f"- {value}")
        break
            
# Working on
# finish code - write up notes/review - upload fully to github (give it a name e.g.)

