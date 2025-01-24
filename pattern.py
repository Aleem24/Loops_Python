



# Right angle pattern
# row = int(input("Enter the number of rows:"))

# for i in range(10,row+1):
#     for j in range(i):
#         print("* ",end="")
#     print()

#Take input from user

num = int(input("Enter the number:"))

# workings of prime or composite checker

if num > 1:
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number ")
        break
    else:
        print(f"{num} is a prime number ")
else:
        print(f"{num} is not a prime number ")
 
