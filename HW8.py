#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW8

#1. Print "Hello World!"
print("heloo")
import random
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a= random.randint(1,10)
b=random.randint(1,10)
c=random.randint(1,10)
lisabc = [a,b,c]
#3. Print A, B, and C on the same line.
print(lisabc)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a > 5:
    print("a is greater than 5")
elif a < 5:
    print("a is less than 5")
else:
    print("a is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if 3 < b < 7:
    print("b is in between 3 and 7")
#6. Make an if statement that prints if variable C is even or odd.
if c % 2 == 0:
    print("c is even")
else:
    print("c is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
threeval = random.randint(1,20) + 3
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if threeval > lisabc:
    print("threeval is greater than lisabc")
elif threeval < lisabc:
    print("threeval is less than lisabc")
    else:
    print("threeval is equal to lisabc")