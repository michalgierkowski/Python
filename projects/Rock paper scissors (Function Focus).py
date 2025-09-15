import random

def intro():                # 1 - intro
    print("Welcome to Rock, Paper, Scissors SHOOT!")
    print("Good luck!")


def get_players_choice():   # 2 - 
    selection = ["Rock", "Paper", "Scissors"]
    while True:
        player_choice = input("Choose --> Rock, Paper or Scissors:  ").capitalize().strip()
        if player_choice not in selection:
            print("Please select one of the options!")
        else:
            return player_choice

        
def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    return computer_choice



def pick_winner(player, computer):
    if player == computer:
        print(f"You chose {player}. Computer chose {computer}. Result = Tie")
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):            # using or \ is good for multiple usuage of conditions within a elif (looks cleaner)
        print(f"{player} beats {computer}.")                        # wrap around each condition with () so python can read it better / doesn't get mixed up
                                                                    # remember to EXACTLY quote the value... not capitalizing made conditions not work at all..
        print("You win this round!")
        return "player win"
    else:
        print(f"{computer} beats {player}.")
        print(f"You lost this round!")
        return "computer win"




def play_round():
    round = 0
    player_score = 0
    computer_score = 0

    while True:
        round += 1
        print(f"Round {round}!")

        players_choice = get_players_choice()
        computer_choice = get_computer_choice()
        result = pick_winner(players_choice, computer_choice)
        print()
        

        if result == "player win":
            player_score += 1
        elif result == "computer win":              # tried conditional expression with assignment operator (in this case += ) python doesn't allow within conditional expressions
            computer_score += 1
            
        print(f"Score: Player {player_score} | Computer {computer_score}")

        print()
        play_again = input("Play again? (y/n):  ").strip().lower()
        

        if play_again == "y":
            continue
        else:
            if player_score == computer_score:
                print(f"Final result: Tie! - Your Score: {player_score} | Computer Score: {computer_score}")
                break
            elif player_score > computer_score:
                print(f"Final result: Win! - Your Score: {player_score} | Computer Score: {computer_score}")
                break
            else:
                print(f"Final result: Loss! - Your Score: {player_score} | Computer Score: {computer_score}")
                break



def main():
    intro() 
    play_round()
    
main()

