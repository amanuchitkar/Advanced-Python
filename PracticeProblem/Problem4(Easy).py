def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the number of choice: "))
    it = []
    for i in range(n):
        num = int(input("Enter your number: "))
        it.append(num)
    print(it)
    for i in range(n):
        print(f"Next palindrome for {it[i]} is {next_palindrome(it[i])}")
