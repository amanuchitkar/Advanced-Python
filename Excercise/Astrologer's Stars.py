try:
    n = int(input("Enter a number: "))
    n2 = int(input("Enter 1 or 0: "))
    n3 = bool(n2)

    if n3 == True:
        for i in range(1, n + 1):
            # for j in range(1, i + 1):
            #     print("* ", end="")
            # print()
            # ---------------or--------------
            print("* " * i)
    elif n3 == False:
        for i in range(n, 0, -1):
            # for j in range(1, i + 1):
            #     print("* ", end="")
            # print()
            # ---------------or---------------------
            print("* " * i)
except Exception as e:
    print("Invalied input!!")
