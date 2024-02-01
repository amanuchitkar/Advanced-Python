import random


def guess(playar):
    rand = random.randint(a, b)
    chance = 0
    while True:
        choice = int(input("Enter your number: "))
        chance += 1
        if choice == rand:
            print(f"Correct you took {chance} trail guess the number ")
            print(f"{playar} take trail {chance}")
            return chance
        elif choice < rand:
            print(f"Wrong guess smaller number ")
        elif choice > rand:
            print("Wrong guess a greater number")
        else:
            print("Something went wrong")


if __name__ == '__main__':
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    playar1 = input("Enter your name:")
    print(f"Please guess the number between {a} and {b}")

    trail_1 = guess(playar1)
    # print(trail_1)
    playar2 = input("Enter your name: ")
    print(f"Please guess the number between {a} and {b}")
    trail_2 = guess(playar2)
    # print(trail_2)
    if trail_1 == trail_2:
        print("You both take same trail")
    elif trail_1 > trail_2:
        print(f"{playar2} win take trail {trail_2} and {playar1} take trail {trail_1}")
    elif trail_1 < trail_2:
        print(f"{playar1} win take trail {trail_1} and {playar2} take trail {trail_2}")
    else:
        print("Something went wrong")
