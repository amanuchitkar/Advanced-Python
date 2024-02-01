n = int(input("Enter the number of apple: "))
mx = int(input("Enter the student minimum number: "))
mn = int(input("Enter the student maximum number: "))
for i in range(mx, mn + 1):
    if mn == mx:
        print(f"This is not in range {mn}={mx}")
    elif n % i == 0:
        print(f"{i} is a divisor of {n}")
    elif n % i >= 1:
        print(f"{i} is not a divisor of {n}")
    else:
        print("Something want wrong")
