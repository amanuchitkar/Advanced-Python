import random


def game_logic(signal_received=None):
    user_score, cop_sore = 0, 0
    i = 1
    chance = int(10)
    while i <= chance:
        user_choice = input("Enter your choice G|S|W: ").upper()
        copu_choice = random.choice(game_opt)
        if user_choice == "EXIT" or user_choice == "EXIT()" or user_choice == signal_received:
            print(exit)
            exit()
        elif user_choice not in game_opt:
            print(f"Invalid input enter proper input, your chance left {10 - i}\n ")
        else:
            print(f"Computer choice is {copu_choice}")
            winning_situation_user = (
                    (user_choice.__eq__("W")) and (copu_choice.__eq__("G")) or
                    (user_choice == "G") and (copu_choice == "S") or
                    (user_choice.__eq__("S")) and (copu_choice.__eq__("W"))
            )
            if user_choice == copu_choice:
                print(f"Tai both choice are same {user_choice}, your chance left {chance - i} out of {chance}\n")
                user_score += 1
                cop_sore += 1
            elif winning_situation_user:
                print(f"You win, your chance left {chance - i} out of {chance}\n")
                user_score += 1
            else:
                print(f"Computer win, your chance left {chance - i} out of {chance}\n")
                cop_sore += 1
        i += 1
    print("<Game over!!>")
    if cop_sore > user_score:
        print("Computer won the series ")
    elif cop_sore == user_score:
        print(f"Tai your both score same ")
    else:
        print("You won the series")
    score_bord = f"Score bord as following:\nYou'r score {user_score}\nComputer score {cop_sore}"
    print(score_bord)


game_opt = ("G", "S", "W")
print("Rules are following:\nYou get 10 chance to play\n    G:gun\n    S:shack\n    W:water\nFor Start write start()"
      "\nFor Exit write exit()")
start = input(": ").upper()
if start == "START()" or start == "START":
    print("\n<GAME START>")
    game_logic()
else:
    print("Invalid input")
