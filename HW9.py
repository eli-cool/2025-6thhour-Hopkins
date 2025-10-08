#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW9


#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
varlis = [a, b, c]
#3. Print the list.
print(varlis)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
larg = varlis[0]
if varlis[0]> varlis[1]:
    if varlis[0] < varlis[2]:
        print(varlis[0],"is the greatest")
    else:
        larg = varlis[2]
        print(varlis[2],"is the greatest")
elif varlis[0] < varlis[1]:
    if varlis[2] < varlis[1]:
        larg = varlis[1]
        print(varlis[1],"is the greatest")
    else:
        larg = varlis[2]
        print(varlis[2],"is the greatest")
else:
    larg = varlis[2]
    print(varlis[2],"is the greatest")

#5. Tie the result (the largest number) from #4 to a variable called "num".
num = larg
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print(num, "is divisible by both 2 and 3")
    else:
        print(num, "is divisible by 2")
elif num % 3 == 0:
    print(num, "is divisible by 3")
else:
    print(num, "is divisible by neither")

