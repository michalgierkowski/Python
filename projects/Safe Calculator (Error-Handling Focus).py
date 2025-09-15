import sys      # quits program


def operator_choice():
    
    while True:

        choice = input("Select your operator -->  + - * / or q (quit):  ").strip().lower()
        if choice in {"+","-","*","/","q"}:                                             # set because unordered,unchangable no duplicates and faster than lists and Tuple
            return choice
        else:
            print("You did not select a valid operator!")   



def user_choices():

    numbers = []


    while True:
        try:
            num1 = float(input("Enter a number:  ").strip())            # allows decimals like real calc    
            break
        
        except ValueError:
            print("Enter a valid value... try again")

    while True:
        try:
            num2 = float(input("Enter another number:  ").strip())      # allows decimals like real calc
            break
        
        except ValueError:
            print("Enter a second valid value... try again")

    numbers.extend([num1, num2])
    return numbers
     



def calculation_operator(numbers,operator):

    a, b = numbers          # unpack list
    if operator == "+": return a + b        # : starts a new block of code
    elif operator == "-": return a - b      # don't need to store it as "result" var as it returns the final result
    elif operator == "*": return a * b    
    elif operator == "/":  
        if b == 0:
            print("You cannot divide by 0")
            return None
        return a / b

                
            
def print_calculation(numbers,operator,result):
    a, b = numbers

    print(f"{a} {operator} {b} = {result}")
    print()


def run_calc():

    
    while True:
        
            operator = operator_choice()
            if operator == "q":
                sys.exit()          # quits program completely 
            else:
                user = user_choices()
                result = calculation_operator(user,operator)
                print_calculation(user,operator,result)
    
run_calc()






# review / notes to take back

# use if = predictable mistakes, like using digits in alpha only inputs
# use try/except = unpredictable exceptions like missing file, bad type cast (like incorrect type)


