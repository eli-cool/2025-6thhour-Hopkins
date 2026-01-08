#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("hi")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("enter number 1"))
b = int(input("enter number 2"))
c = int(input("enter number 3"))
#4. Add a and b together, then divide the sum by c. Print the result.
d = (a + b) / c
#5. Round the result from #3 up or down, and then determine if it is even or odd.
d = round(d)
if d % 2 == 0:
    print("even")
else:
    print("odd")

#6. Create a list of five different random integers between 1 and 10.
lis = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),]
#7. Print the 4th number in the list.
print(lis[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
lis.append(random.randint(1,10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
lis.sort()
print(lis[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
h = 1
while h < 100:
    print(h)
    h *= 2
#11. Create a list containing the names of five other students in the classroom.
names = ["Ally","Alaya","GREG","Conor","Ethan"]
#12. Create a for loop that individually prints out the names of each student in the list.
for i in names:
    print(i)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
m = 1
for m in range(1,100):
    print(m)
    m += 1
    if m % 10 == 0:
        print("hi")
        break
#14. Free space. Do something creative. :)
#i have a game to make