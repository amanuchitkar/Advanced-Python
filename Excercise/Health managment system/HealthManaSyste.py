def getdate():
    import datetime

    return datetime.datetime.now()


t = getdate()


def nayanfood(var1):
    if var1 == "1":
        inp = input("What Nayan Eat:")
        f = open("nayanFood.txt", "a")
        f.write(str(t))
        f.write(" Nayan Eat : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var1 == "2":
        f = open("nayanFood.txt", "rt")
        r = f.read()
        print(r)
        f.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def amanfood(var1):
    if var1 == "1":
        inp = input("What Aman Eat:")
        f = open("amanFood.txt", "a")
        f.write(str(t))
        f.write(" Aman Eat : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var1 == "2":
        f = open("amanFood.txt", "rt")
        r = f.read()
        print(r)
        f.close()
    else:
        print("You choose something wrong, Please choose correct order ")


def nayanExersice(var2):
    if var2 == "1":
        inp = input("What Nayan done: ")
        f = open("nayanExe.txt", "a")
        f.write(str(t))
        f.write(" Nayan done : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var2 == "2":
        f = open("nayanExe.txt", "rt")
        r = f.read()
        print(r)
        f.close()


def amanExersice(var2):
    if var2 == "1":
        inp = input("What Aman done: ")
        f = open("amanExe.txt", "a")
        f.write(str(t))
        f.write(" Aman done : ")
        f.write(str(inp))
        f.write("\n")
        f.close()
    elif var2 == "2":
        f = open("amanExe.txt", "rt")
        r = f.read()
        print(r)
        f.close()


print("Choose a person")
print("1.Nayan\n2.Aman\n3.Mrudul\n4.pranav")
per = input(": ")
print("For what: ")
print("1.Food\n2.Exersice")
cho = input(": ")
print("1.Log\n2.Retrive")
var = input(": ")
if per == "1":
    if cho == "1":
        if var == "1" or var == "2":
            nayanfood(var)
    elif cho == "2":
        if var == "1" or var == "2":
            nayanExersice(var)
elif per == "2":
    if cho == "1":
        if var == "1" or var == "2":
            amanfood(var)
    elif cho == "2":
        if var == "1" or var == "2":
            amanExersice(var)
else:
    print("You choose something wrong, Please choose correct order ")
