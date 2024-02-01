# def Age():
#     a = int(input("Enter your age or DOB: "))
#     if a < 0:
#         print("you not born at .")
#     elif 100 < a < 125:
#         print("you are lucky person alive..")
#     elif a == 100:
#         print("You already complete 100 congratulation,you are lucky person alive..")
#     elif 1 <= a < 100:
#         print(f"You complete 100 year after {100 - a} year ")
#     else:
#         print("invalid input!!!")


# def DOB():
#     a = int(input("Enter your age or DOB: "))
#     if a == 2022:
#         print("you not born at .")
#     elif 1000 < a < 2022:
#         print(f"Your current age is {2022 - a}")
#     else:
#         print("invalid input!!!")


# while True:
#     choice = int(input("1.For age\n2.For DOB\n3.For exit\n: "))

#     if choice == 1:
#         Age()
#     elif choice == 2:
#         DOB()
#     elif choice == 3:
#         print(exit())
#         exit()
#     else:
#         print("invalid input!!")


# ---------------------------cWh_______________________________

yearage = int(input("Enter your age or DOB: "))
isage = False
isyear = False

if len(str(yearage)) == 4:
    isyear = True
else:
    isage = True

if yearage < 1900 and isyear:
    print("You seem oldest person alive")
elif yearage > 2022:
    print("You not born yet")

if isage:
    yearage = 2022 - yearage

print(f"You will be 100 year old in {yearage + 100} ")
interestedYear = int(input("Enter the year you want to know your age in: "))
print(f"You will be {interestedYear - yearage} year old in {interestedYear}")
