import os


def system(path, fileN, forme):
    os.chdir(path)
    f = open(fileN)
    read = f.read().split()
    f.close()
    count = 1
    for i in os.listdir(path):
        fname, Forma = os.path.splitext(i)

        if Forma == f".{forme}":
            newname = f"{str(count)}{Forma}"
            count += 1
            os.rename(i, newname)

        elif fname not in read:
            ti = fname.title()
            Newname = f"{ti}{Forma}"
            os.rename(i, Newname)
        else:
            sm = fname.lower()
            NewName = f"{sm}{Forma}"
            os.rename(i, NewName)


p = input("path: ")
f = input("file name: ")
e = input("file format: ")
system(p, f, e)
