#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip():
    global heads, tails
    for i in range(1,100):
        pick = random.choice(["heads","tails"])
        if pick == "heads":
            heads += 1
        else:
            tails += 1
        print(pick, heads, tails)
#4. Call the "Hello world" and "Coin Flip" functions here
flip()
#5. Print the final result of heads and tails here
print("final result: ", heads ,"heads", tails, "tails")
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["blue","red","yellow","green","purple"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def pullBag():
    print(beanBag)
    pull = random.choice(beanBag)
    print(pull,"was removed")
    beanBag.remove(pull)
    pullloop()
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def pullloop():
        ask = input("Do you wish to pull? (yes/no): ")
        if ask == "yes":
            if beanBag:
                pullBag()
            else:
                print("no more beans!!")

#9. Call the "Bean Pull" function here
pullloop()