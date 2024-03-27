row=5
# for i in range(1,row):
#     print(' '*(row-i)+'*'*(2*i-1))

# for i in range(row,0,-1):
#     print(' '*(row-i)+'*'*(2*i-1))

# for i in range(1,row):
#     print(" "*(row-i)+"* "*i)

# for i in range(row,0,-1):
#     print(' '*(row-i)+'* '*i)

# i = 1
# while i <= row:
#         # Print leading spaces
#         j = 1
#         while j <= row-i:
#             print(" ", end="")
#             j += 1
#         # Print stars
#         k = 1
#         while k <= 2*i-1:
#             print("*", end="")
#             k += 1
#         print()  # Move to the next line
#         i += 1


# i = row
# while i >= 1:
#         # Print leading spaces
#         j = 1
#         while j <= (row - i):
#             print(" ", end="")
#             j += 1
#         # Print stars
#         k = 1
#         while k <= (i - 1):
#             print("* ", end="")
#             k += 1
#         print()  # Move to the next line
#         i -= 1



#Dimond
# for i in range(1,row):
#     print(' '*(row-i)+"*"*(2*i-1))
# for i in range(row,0,-1):
#     print(' '*(row-i)+"*"*(2*i-1))

# i=1
# while i<=row:
#     j=1
#     while j<=row-i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=(2*i-1):
#         print("*",end="")
#         k+=1
#     i+=1
#     print()

# i=row-1
# while i>=1:
#     j=1
#     while j<=row-i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=(2*i-1):
#         print("*",end="")
#         k+=1
#     i-=1
#     print()

for i in range(row):
    print()
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end='')
        
for i in range(row,0,-1):
    print()
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end='')