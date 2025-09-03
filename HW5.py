#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW5
import statistics
#1. Create a list with 9 different numbers inside.
numlis=[6,7,5,9,1,10,4,3,8]
#2. Sort the list from highest to lowest.
numlis.sort(reverse=True)
#3. Create an empty list.
emp=[]
#4. Remove the median number from the first list and add it to the second list.
emp.append(numlis.pop(len(numlis)//2))
#5. Remove the first number from the first list and add it to the second list.
emp.append(numlis.pop(0))
#6. Print both lists.
print(numlis)
print(emp)
#7. Add the two numbers in the second list together and print the result.

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

#9. Sort the first list from lowest to highest and print it.