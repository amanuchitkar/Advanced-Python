def getdate():
    import time

    return time.asctime(time.localtime(time.time()))


t = getdate()


def food(var):
    if var == "1":
        print("For what ?\n")
        print("1. Log\n2. Retrive")
        imp = input()
        if imp == "1":
            inp = input("What Harry Eat: ")
            with open("HarryFood.txt", "a") as apa:
                apa.write(str(t))
                apa.write(" Harry Eat : ")
                apa.write(str(inp))
                apa.write("\n")
        elif imp == "2":
            with open("HarryFood.txt") as ra:
                r = ra.read()
                print(r)
    elif var == "2":
        print("For what? ")
        print("1. Log\n2. Retrive")
        imp = input(": ")
        if imp == "1":
            inp = input("What Rohan Eat: ")
            with open("RohanFood.txt", "a") as apa:
                apa.write(str(t))
                apa.write(" Rohan Eat: ")
                apa.write(str(inp))
                apa.write("\n")
        elif imp == "2":
            with open("RohanFood.txt") as ra:
                r = ra.read()
                print(r)
    elif var == "3":
        print("For what? ")
        print("1. Log\n2. Retrive")
        imp = input(": ")
        if imp == "1":
            inp = input("What Harmman Eat: ")
            with open("HarmmanFood.txt", "a") as apa:
                apa.write(str(t))
                apa.write(" Harmman Eat: ")
                apa.write(str(inp))
                apa.write("\n")
        elif imp == "2":
            with open("HarmmanFood.txt") as ra:
                r = ra.read()
                print(r)
    else:
        print("You choose something wrong, Please choose correct order ")


def exercise(var):
    if var == "1":
        print("For what? ")
        print("1. Log\n2. Retrive")
        imp = input(": ")
        if imp == "1":
            inp = input("What Harry done: ")
            with open("HarryExe.txt", "a") as apa:
                apa.write(str(t))
                apa.write(" Harry done : ")
                apa.write(str(inp))
                apa.write("\n")
        elif imp == "2":
            ra = open("HarryExe.txt")
            r = ra.read()
            print(r)
            ra.close()
    elif var == "2":
        print("For what? ")
        print("1. Log\n2. Retrive")
        imp = input(": ")
        if imp == "1":
            inp = input("What Rohan done: ")
            with open("RohanExe.txt", "a") as apa:
                apa.write(str(t))
                apa.write(" Rohan done : ")
                apa.write(str(inp))
                apa.write("\n")
        elif imp == "2":
            ra = open("RohanExe.txt")
            r = ra.read()
            print(r)
            ra.close()
    elif var == "3":
        print("For what? ")
        print("1. Log\n2. Retrive")
        imp = input(": ")
        if imp == "1":
            inp = input("What Harmman done: ")
            with open("HarmmanExe.txt", "a") as apa:
                apa.write(str(t))
                apa.write(" Harmman done : ")
                apa.write(str(inp))
                apa.write("\n")
        elif imp == "2":
            ra = open("HarmmanExe.txt")
            r = ra.read()
            print(r)
            ra.close()
    else:
        print("You choose something wrong, Please choose correct order ")


print("What do you want ?")
print("1. Food\n2. Exercise")
var = input(": ")
print("Choose Persone: ")
print("1. Harry\n2. rohan\n3. Harmman")
per = input(": ")

if var == "1":
    food(per)
elif var == "2":
    exercise(per)
else:
    print("You choose something wrong, Please choose correct order ")
