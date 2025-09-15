# 1. Grabbing passwords from user

def user_password():

    passwords = []      # using [] a list if I did () <-- a tuple, it wouldn't allow new values (no .append)

    while True:
        num_passwords = input("Number of passwords to analyze >   ").strip()

        if num_passwords.isdigit():
            num_passwords = int(num_passwords)
            break
        
        else:
            print("Please enter a number.")
    
    
    for num in range(num_passwords):
        
        
        password = input(f"{num + 1} - Evaulate your password >  ").replace(" ", "").strip()
        passwords.append(password)
    
        if len(passwords) == num_passwords:
            return passwords
        
        
# 2. Checks passwords against each rules

def check_password_rules(password_details):
    
    
    password_scores = []
    special_chars = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="}

    
    for password in password_details:
        score = 0 # stores a new score for each loop (for each password in list)

        if 8 <= len(password) < 64:
            score += 1

        # any() function new concept- if ANY of X in X (in this code atleast) give a score

        if any(char.isupper() for char in password): # checks if atleast 1 character is upper
            score += 1
        
        if any(char.islower() for char in password):
            score += 1
        
        if any(char.isdigit() for char in password): 
            score += 1
        
        if any(char in special_chars for char in password):
            score += 1

        password_scores.append((password, score))  # stored as tuple, unchangeable and great for groups of value (like pairs)
        
    return password_scores




# 3. Evaulates score (is it weak, medium weak , strong etc)
# need to unpack it and give it rating (weak, med,strong) out of 5 rules - maybe a return into new list?

def strength_score(password_details):

    results = []

    for password, score in password_details:
        if score == 5:
            strength = "Very Strong"
        elif score == 4:
            strength = "Strong"
        elif score == 3:
            strength = "Average"
        elif score == 2:
            strength = "Weak"
        else:
            strength = "Very Weak"

        results.append((password, score, strength))

    return results


# 4. Common password checks if password is within a "common password lists" and returns true or false value 


def common_passwords(password_details):

    results = []

    common_passwords_top10 = {
    "123456",
    "123456789",
    "12345678",
    "password",
    "qwerty123",
    "qwerty1",
    "111111",
    "12345",
    "secret",
    "123123"
 }
    
    for password, score, strength in password_details:       # unpacking
        if password in common_passwords_top10:
            common = True
        else:
            common = False

        results.append((password,score,strength,common))

    return results


# asks user for how many guesses per second

def guesses_per_sec():

    while True:

        guesses = input("How many gusses per second? >  ").replace(".","").strip()

        if not guesses.isdigit():
            print("Enter a whole number")
        
        else:
            return int(guesses)
 


# 5. brute force need to work out the forumla for this etc and find out


def time_to_crack(password_details, guesses):

    results = []

    special_chars = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="}

    for password, score, strength, common in password_details:
        character_set_size = 0

        if any(char.islower() for char in password):       # don't need to use type cast since "password" is a str
            character_set_size += 26
        
        if any(char.isupper() for char in password):
            character_set_size += 26
        
        if any(char.isdigit() for char in password):
            character_set_size += 10

        if any(char in special_chars for char in password):
            character_set_size += len(special_chars)        # faster than "14"
        
        #calc
        total_combinations = (character_set_size) ** len(password)
        time = total_combinations / guesses

        results.append((password, score, strength, common, time))
    
    return results


# 6. secs/mins/hrs/days+

def time_convert(password_details):

    results = []

    for password, score, strength, common, time in password_details:
        

        time = int(time)

        if time < 60:
            time = f"{time} seconds"
        
        elif time < 3600:
            time /= 60
            time = f"{time} minutes"

        elif time < 86400:
            time /= 3600
            time = f"{time} hours"

        elif time < 31536000:
            time /= 86400
            time = f"{time} days"

        else:
            time /= 31536000
            time = f"{time:.1f} years"

        
        results.append((password, score, strength, common, time))

    return results


#  7 do suggestions then do final print
        
def suggestions(password_details):
    special_chars = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="}
    results = []

    for password, score, strength, common, time in password_details:
        suggestion_list = []        # every loop --> suggestions for each password get stored

        if not any(char.islower() for char in password):
            suggestion_list.append("add lowercase letters")

        if not any(char.isupper() for char in password):
            suggestion_list.append("add uppercase letters")

        if not any(char.isdigit() for char in password):
            suggestion_list.append("add digits")

        if not any(char in special_chars for char in password):
            suggestion_list.append("add special characters")

        if len(password) < 12:  
            suggestion_list.append("make it longer than 12 characters")

        if suggestion_list:
            suggestion = ", ".join(suggestion_list)
        else:
            suggestion = "None, this is a strong password."

        results.append((password, score, strength, common, time, suggestion))

    return results



def output(password_details):

    for password, score, strength, common, time, suggestion in password_details:
        print("---------------------------------------")
        
        
        print(f"Analyzing: {password}")
        print(f"Score: {score}/5")
        print(f"Strength: {strength}")
        print(f"Common password: {common}")
        print(f"Estimated Brute Force: {time}")
        print(f"Suggestions: {suggestion}")


        print("---------------------------------------")
 
        



def run_program():
    
    while True:
        
        print(
            
        )
        start = input("Type start to begin the program... ").strip().lower()

        if start == "start":
            passwords = user_password()
            rule_score = check_password_rules(passwords)


            strength = strength_score(rule_score)

            common = common_passwords(strength)
            guesses = guesses_per_sec()

            crack_time = time_to_crack(common, guesses)

    
            converted_time = time_convert(crack_time)
            final_results = suggestions(converted_time)
            output(final_results)
    
            print("Analysis done.")
        else:
            break
    
run_program()


# review

# function 2 - don't need to add type cast (str) due to it already being a string
# functions 2,4,5,7 - changed [list] to a {set} - as these char are unique, and lists are slower in general
# (try to use lists last, focus on set and tuple)






