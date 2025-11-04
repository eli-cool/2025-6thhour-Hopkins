#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW12
import random
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
    if i <= 0:
        print("hellow")
        break
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
x = 30
while x >= 0:
    if x % 2 == 0:
        print(x)
    x -= 1

print("end of loop")

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
y = 30
while y >= 0:
    if y % 3 == 0:
        print(y)
    y -= 1

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
ran = int
while ran != 1:
    ran = random.randint(1,6)
    print("the random number is:")
    print(ran)
#5. Create a while loop that asks for a number input until the user inputs the number 0.
ask = int
while ask != 0:
    ask = int(input("enter your number: "))
    print("your number is:",ask)
print("you said 0 which ends everything")