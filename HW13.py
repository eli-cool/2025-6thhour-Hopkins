#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".
num = 0
sen = ""
#Create a while loop that follows the rules of the game.
while num <= 100:
    if num % 3 == 0:
        sen += "fizz"
    if num % 5 == 0:
        sen += "buzz"
    if not sen:
        print(num)
    else:
        print(sen)

    num += 1
    sen = ""
print("ended loop")