# for i in range(1,11):
#     for j in range(1,11):
#         print("* ",end="")
#     print()



# Right angle pattern
row = int(input("Enter the number of rows:"))

for i in range(1,row+1):
    for j in range(i):
        print("*",end="")
    print()