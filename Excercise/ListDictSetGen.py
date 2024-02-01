noOfList = int(input("How many element you want to add\n"))

choice = str(input('''
Which type of Comprehension you want to create?
A. For List Comprehension
B. For Dictionary Comprehension
C. For Set Comprehension
D. For Generator Comprehension
: ''')).upper()
inp_element = input("Enter elements separated by space:")
lis = inp_element.split()
j = 0
if choice == "A":
    if noOfList >= len(lis):
        lists = [i for i in lis]
        print(lists)
    else:
        print("your element and are wrong try agent")
elif choice == "B":
    if noOfList >= len(lis):
        dict = {j: f"item{len(j)-3}" for j in lis}
        j+=1
        print(dict)
    else:
        print("your element and are wrong try agent")
elif choice == "C":
    if noOfList >= len(lis):
        set = {i for i in lis}
        print(set)
    else:
        print("your element and are wrong try agent")
elif choice == "D":
    if noOfList >= len(lis):
        gen = (i for i in lis)
        print(gen)
        for i in gen:
            print(i)
    else:
        print("your element and are wrong try agent")

else:
    print("your element and are wrong try agent")
