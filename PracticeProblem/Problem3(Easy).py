l = input("Enter numbers: ")
# l = "1,2,3,4"
lists = l.split(',')
print(lists)

a1 = lists.copy()
a1.sort()
print(f"Using sort(): {a1}")

a = lists.copy()
a.reverse()
print(f"Using reverse(): {a}")

b = lists.copy()
c = b[::-1]
print(f"Using [::-1]: {c}")

d = lists.copy()
for i in range(len(lists)//2):
    d[i], d[len(d)-i-1] = d[len(d)-i-1], d[i]
print(f"Using for loop: {d}")
