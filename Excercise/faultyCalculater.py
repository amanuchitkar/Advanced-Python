print("Enter two numbers: ")
num1 = int(input())
num2 = int(input())
marke = input("Enter which proprety you want to do: ")
if marke == "+":
    if num1 == 56 and num2 == 9:
        print("56 + 9 = 77")
    elif num1 == 9 and num2 == 56:
        print("9 + 56 = 77")

    else:
        print(num1, "+", num2, "=", num1 + num2)
elif marke == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif marke == "*":
    if num1 == 45 and num2 == 3:
        print("45 * 3 = 555")
    elif num1 == 3 and num2 == 45:
        print("3 * 45 = 555")
    else:
        print(num1, "*", num2, "=", num1 * num2)
elif marke == "/":
    if num1 == 56 and num2 == 6:
        print("56 / 6 = 4")
    else:
        print(num1, "/", num2, "=", num1 / num2)
else:
    print("inapropriat input!!!!!")
