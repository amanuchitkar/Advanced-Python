def kmmiles(num, value):
    if value == "km":
        return f"{int(num * 0.62137119)} miles"
    elif value == "miles":
        return f"{int(num * 1.609344)} km"
    elif value == "c":
        return f"{int((num * 9 / 5) + 32)}°F"
    elif value == "f":
        return f"{int(((num - 32) * 5) / 9)}°C"
    elif value == "cm":
        return f"{int(num / 2.54)} inches"
    elif value == "inches":
        return f"{int(num * 2.54)} cm"
    elif value == "lbs":
        return f"{int(num * 0.45359237)} kg"
    elif value == "kg":
        return f"{int(num * 2.2)} lb"
    else:
        return "Somthing wants wrong"


inp = str(input("Enter value you you want to convert(use space): ")).lower()
lists = inp.split(" ")
print(kmmiles(int(lists[0]), lists[1]))
