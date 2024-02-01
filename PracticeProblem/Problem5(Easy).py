def next_palindrome(n):
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter your choice number: "))
    lists = []
    for i in range(n):
        numbers = int(input("Enter your number: "))
        lists.append(numbers)

    print(f"input = {lists}")
    print(f"Output List: {[lists[i] if lists[i] < 10 else next_palindrome(lists[i]) for i in range(n)]}")

