numberOfGuess = 1
print("You get 9 guess")
while numberOfGuess <= 9:
    if numberOfGuess == 9:
        print("Last Guess :", end="")

    else:
        print("Guess NO.", numberOfGuess, ":", end="")
    numberOfGuess = numberOfGuess + 1

    inpu = int(input())
    if inpu > 18:
        print("Grater then the value!!!")
    elif inpu == 18:
        print(
            "Congratulation you are winner\nNo.",
            numberOfGuess - 1,
            "Guess you tack to win",
        )
        break
    else:
        print("lesser then !")
if numberOfGuess > 9:
    print("Game over!!!!")
