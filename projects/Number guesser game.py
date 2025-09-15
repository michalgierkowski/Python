import random



def intro():           
    name = input("Welcome to the guessing game! Let's start with your name:  ")
    print(f"Hello {name}!")
    print("The rules are simple: ")
    print("Guess the secret number (1 - 10)")
    print("and have fun!")
    return name


def get_guess():
    while True:
        guess = input("Enter a number:  ").strip()          # string methods only work on strings
        if guess.isdigit():                                 # remember if you want to add a "law" it has to be inside a function
            return int(guess)
        else:
            print("Please enter a numbers only!")
    



def check_guess(secret, guess):
    
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")



def play_game():
    
    name = intro()
    secret = random.randint(1, 10)
    attempts = 0

    
    while True:
        guess = get_guess()
        attempts += 1
        if guess != secret:
            check_guess(secret, guess)
        else:
            print(f"You are correct!")
            print(f"{name.upper()}... it took you {attempts} attempts!")
            
            play_again = input("Would you like to play again? (y/n):  ").lower().strip()

            if play_again == "y":
                continue
            else:
                break
     

play_game()















