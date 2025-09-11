#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print("hi")
#3. Create three different variables that each randomly generate an integer between 1 and 10
ran1 = random.randint(1,10)

ran2 = random.randint(1,10)

ran3 = random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(ran1,ran2,ran3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
ran1 += 2
ran2 -= 4
ran3 *= 1.5
#6. Print each result from #5 on the same line.
print(ran1,ran2,ran3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

fourlist = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
fourlist.sort()
print(fourlist)
#9. Add together the highest three numbers in the list from #7 and print the result.
lishigh = sum(fourlist[-3:])
print(lishigh)
#10. Create a list with 5 names of other students in this class and print the list.
names = ["eli","ally","alaya","brodie", "devon"]
#11. Shuffle the list in #10 and print the list again.
shuffle(names)
print(names)
#12. Print a random choice from the list of names from #10.
print(random.choice(names))