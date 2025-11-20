# list to store user values
values = []

# Input 1
# Using expections allocates more memory
# Causes code to be slower and less efficient
# And less readable
#while True:
    #try:
        #userInput = int(input("""Would you like to enter:
    #1. Text
    #2. Number
    #Your choice -->  """))
        #break
    #except ValueError:
        #print("You did not enter a valid input.")

# Input 2 
# Writing code with less expection
# Makes it more efficient than Input 1
# And readable


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
    "1. Store a string \n"
    "2. Store a number \n"
    "3. View next page \n"
    "Enter here:  ")

    # calling up our function
    checkUserInput(userInput)

    if userInput == "1":
        # a string can involve numeric or alphabetical units
        text = input("Enter a string of your choice:  ")
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
        "1. View only strings?\n"
        "2. View only numbers?\n"
        "3. View both?\n"
        "Select your option -->  ")

    # calling our function again
    checkUserInput(userRequest)

    if userRequest == "1":
        for value in values:
            if value == str(value):
                print(value)
                

    elif userRequest == "2":
        for value in values:
            if value == int(value):
                print(value)
                



# finish the last "would you like to" steps 
# Clean up code, add any "errors handling" with minimizing memory allocation keeping it clean and readable

