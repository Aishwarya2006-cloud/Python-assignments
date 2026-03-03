#1
print("task 1:")
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
    
# 1
# 22
# 333
# 4444
# 55555
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()
    
# 1
# 21
# 321
# 4321
# 54321
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
    
# 2
# 4 6
# 8 10 12
# 14 16 18 20
row=4
num=2
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 2
    print()

# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
    
#2
print("2:")
# A
# AB 
# ABC
# ABCD
# ABCDE
for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()
    
# *
# * #
# * # *
# * # * #
# * # * # *
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()

# P 
# YY 
# TTT 
# HHHH
# OOOOO 
# NNNNNN
chars = ['P', 'Y', 'T', 'H', 'O', 'N']
for i in range(6):
    for j in range(i + 1):
        print(chars[i], end="")
    print()
    
# P 
# PY 
# PYT
# PYTH
# PYTHO
# PYTHON
chars = ['P', 'Y', 'T', 'H', 'O', 'N']
for i in range(6):
    for j in range(0, i + 1):
        print(chars[j], end="")
    print()
    
#3
print("3:")
n=int(input("Enter the number: "))
for i in range(1, n+1):
    print(i,end=" ")
print()
# 4
print("4:")
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
    
# 5
print("5:")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
    
# 6
print("6:")

rows = 5
for i in range(1, rows + 1):
    print("*"*i)
for k in range(rows-1,0,-1):
    print("*"*k)

# 7
print("7:")
#write a program that find and print all the prime numbers between two number entered by the user.Use a while loop to take input and validate it, and a for loop to check for primality.
while True:
    N1=int(input("Enter the first number: "))
    N2=int(input("Enter the second number: "))
    if N1<N2:
        break
    print("Invalid input. The first number must be less than the second number.")
print("Prime numbers between %d and %d are:"%(N1,N2))
for num in range(N1, N2 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
        
        